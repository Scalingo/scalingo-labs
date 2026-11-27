package main

import (
	"bytes"
	"encoding/binary"
	"encoding/json"
	"errors"
	"io"
	"log"
	"net"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

// Max. file size is 10 MiB
const maxFileSize = 10 * 1024 * 1024


func main() {
	clamavHost := os.Getenv("CLAMAV_HOST")
	if clamavHost == "" {
		log.Fatal("CLAMAV_HOST is required")
	}
	clamavPort := os.Getenv("CLAMAV_PORT")
	if clamavPort == "" {
		clamavPort = "3310"
	}
	clamavPortNumber, err := strconv.Atoi(clamavPort)
	if err != nil || clamavPortNumber < 1 || clamavPortNumber > 65535 {
		log.Fatal("CLAMAV_PORT must be a port number between 1 and 65535")
	}
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	server := &http.Server{
		Addr:              net.JoinHostPort("", port),
		Handler:           scanHandler(net.JoinHostPort(clamavHost, strconv.Itoa(clamavPortNumber))),
		ReadHeaderTimeout: 10 * time.Second,
	}
	log.Printf("Listening on %s", server.Addr)
	log.Fatal(server.ListenAndServe())
}

// scanFile streams a file using ClamAV's INSTREAM protocol.
func scanFile(address string, file io.Reader) (string, error) {
	conn, err := net.DialTimeout("tcp", address, 30*time.Second)
	if err != nil {
		return "", err
	}
	defer conn.Close()

	write := func(data []byte) error {
		if err := conn.SetWriteDeadline(time.Now().Add(60 * time.Second)); err != nil {
			return err
		}
		for len(data) > 0 {
			n, err := conn.Write(data)
			if err != nil {
				return err
			}
			if n == 0 {
				return io.ErrShortWrite
			}
			data = data[n:]
		}
		return nil
	}
	if err := write([]byte("zINSTREAM\x00")); err != nil {
		return "", err
	}

	chunk := make([]byte, 8192)
	var length [4]byte
	for {
		n, readErr := file.Read(chunk)
		if n > 0 {
			binary.BigEndian.PutUint32(length[:], uint32(n))
			if err := write(length[:]); err != nil {
				return "", err
			}
			if err := write(chunk[:n]); err != nil {
				return "", err
			}
		}
		if readErr != nil {
			if readErr != io.EOF {
				return "", readErr
			}
			break
		}
	}
	if err := write([]byte{0, 0, 0, 0}); err != nil {
		return "", err
	}

	var response []byte
	buffer := make([]byte, 4096)
	for {
		if err := conn.SetReadDeadline(time.Now().Add(60 * time.Second)); err != nil {
			return "", err
		}
		n, err := conn.Read(buffer)
		response = append(response, buffer[:n]...)
		if end := bytes.IndexByte(response, 0); end >= 0 {
			return strings.ToValidUTF8(string(response[:end]), "\uFFFD"), nil
		}
		if err != nil {
			if err != io.EOF {
				return "", err
			}
			break
		}
	}
	if len(response) == 0 {
		return "", errors.New("empty ClamAV response")
	}
	return strings.ToValidUTF8(string(response), "\uFFFD"), nil
}

func writeJSON(w http.ResponseWriter, status int, body map[string]string) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(body)
}

func scanHandler(address string) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/scan" {
			http.NotFound(w, r)
			return
		}
		if r.Method == http.MethodOptions {
			w.Header().Set("Allow", "POST, OPTIONS")
			w.WriteHeader(http.StatusOK)
			return
		}
		if r.Method != http.MethodPost {
			w.Header().Set("Allow", "POST, OPTIONS")
			http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
			return
		}
		r.Body = http.MaxBytesReader(w, r.Body, maxFileSize)
		if r.ContentLength > maxFileSize {
			http.Error(w, "Request Entity Too Large", http.StatusRequestEntityTooLarge)
			return
		}
		err := r.ParseMultipartForm(maxFileSize)
		if r.MultipartForm != nil {
			defer r.MultipartForm.RemoveAll()
		}
		if err != nil {
			var sizeErr *http.MaxBytesError
			if errors.As(err, &sizeErr) {
				http.Error(w, "Request Entity Too Large", http.StatusRequestEntityTooLarge)
			} else {
				writeJSON(w, http.StatusBadRequest, map[string]string{"error": "No file provided"})
			}
			return
		}
		file, _, err := r.FormFile("file")
		if err != nil {
			writeJSON(w, http.StatusBadRequest, map[string]string{"error": "No file provided"})
			return
		}
		defer file.Close()

		result, err := scanFile(address, file)
		switch {
		case err != nil:
			writeJSON(w, http.StatusServiceUnavailable, map[string]string{
				"status": "error", "message": "Antivirus service unavailable",
			})
		case result == "stream: OK":
			writeJSON(w, http.StatusOK, map[string]string{
				"status": "clean", "message": "No malware detected",
			})
		case strings.HasPrefix(result, "stream: ") && strings.HasSuffix(result, " FOUND"):
			writeJSON(w, http.StatusOK, map[string]string{
				"status": "infected", "threat": strings.TrimSuffix(strings.TrimPrefix(result, "stream: "), " FOUND"),
			})
		default:
			writeJSON(w, http.StatusServiceUnavailable, map[string]string{
				"status": "error", "message": "Antivirus scan could not be completed",
			})
		}
	})
}
