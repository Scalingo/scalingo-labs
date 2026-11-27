# ClamAV File-Scanning API

This very small app allows to test a ClamAV deployment, such as the one we
describe in Scalingo [ClamAV tutorial][clamav-tutorial].

The app provides a simple HTTP endpoint for checking files for malware, using
ClamAV. It accepts a multipart file upload in the file field of a `POST`
`/scan` request. It then streams the file to a ClamAV daemon over TCP using the
INSTREAM protocol, and returns a JSON response indicating whether the file is
clean or infected, including the detected threat name.

Upload requests are limited to 10 MiB, including multipart overhead.

Written in Go using only the standard library, the app connects to the daemon
specified by `CLAMAV_HOST` and `CLAMAV_PORT` (default: `3310`) and listens on
`PORT`.


## Deploying the App

1. Sparse-checkout the `scalingo-labs` repository, and extend it by downloading
   the directory containing the code for this demo:
   ```shell
   git clone --sparse https://github.com/Scalingo/scalingo-labs
   cd scalingo-labs
   git sparse-checkout set clamav
   cd clamav
   ```

2. Create a new git repository from the downloaded `clamav` directory:
   ```shell
   git init
   git add .
   git commit --message "Initialize file-scanning app"
   ```

3. Create the application on Scalingo, in the same project hosting your ClamAV
   instance:
   ```shell
   scalingo create my-clamav-api --project-id $project-id
   ```

4. Set mandatory environment variables, allowing to point the API to the ClamAV
   instance.

   - For `$host`, we strongly advise to use a process type domain name, such as
     `clamav.<application_id>.<private_network_id>.private-network.internal`.
     This would allow the app to benefit from multiple ClamAV containers, if
     you were to scale horizontally.

     To retrieve this domain name using the CLI:
     ```shell
     scalingo --app my-clamav private-networks-domain-names
     ```

     The output should look like this:
     ```shell
     ┌────────────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
     │ CONTAINER TYPE │                                                    DOMAIN NAME                                                     │
     ├────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
     │ clamav         │ clamav.ap-588c4c3e-f454-4379-903b-a6eab01f8291.pn-5b3a072d-dd14-4a05-821c-0c2754acef04.private-network.internal.   │
     │ clamav         │ 1.clamav.ap-588c4c3e-f454-4379-903b-a6eab01f8291.pn-5b3a072d-dd14-4a05-821c-0c2754acef04.private-network.internal. │
     └────────────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
     ```

     Avoid using the domain name starting with a number, which designates a
     precise single container. Instead, use the one starting with the process
     type name, which designates the pool of available containers.

   - For `$port`, use the one defined in your ClamAV app, or use the default
     one (`3310`).

   ```shell
   scalingo --app my-clamav-api env-set CLAMAV_HOST=$host
   scalingo --app my-clamav-api env-set CLAMAV_PORT=$port
   ```

5. Trigger a deployment to Scalingo:
   ```shell
   git push scalingo main
   ```

6. Test everyting is working:

   - With a clean file:
     ```shell
     curl -i -F 'file=@/tmp/clamav-test.txt' https://my-clamav-api.osc-fr1.scalingo.io/scan
     ```
     ```shell
     HTTP/2 200 
     date: Fri, 27 Nov 2026 10:33:14 GMT
     content-type: application/json
     content-length: 51
     x-request-id: 02c9f909-b029-49b3-9a19-d208ff151bd2

     {"message":"No malware detected","status":"clean"}
     ```

   - With the [EICAR Anti-Virus test file][eicar]:
     ```shell
     curl -i -F 'file=@/tmp/eicar.com.txt' https://my-clamav-api.osc-fr1.scalingo.io/scan
     ```
     ```shell
     HTTP/2 200 
     date: Fri, 27 Nov 2026 10:32:46 GMT
     content-type: application/json
     content-length: 54
     x-request-id: 831cec22-d394-4173-bbaf-69613e14583d

     {"status":"infected","threat":"Eicar-Test-Signature"}
     ```


## Protecting the App

It is strongly recommended to restrict access to the API to trusted clients.
This can be achieved by configuring [Application
Firewall][application-firewall] to allow incoming requests only from authorized
IP addresses or networks. Additionally, the API should be served [over
HTTPS][force-https] only to protect files in transit.

While these two first elements can be achieved directly thanks to Scalingo's
features (see hereafter), a few others will most probably land on your side:

An authentication mechanism (such as API keys or ) should be
implemented to prevent unauthorized access, even from trusted networks.

Since file scanning can be resource-intensive, additional safeguards should
ideally be implemented to mitigate abuse and denial-of-service attacks. These
include rate limiting, maximum upload size restrictions, request timeouts, and
limits on the number of concurrent scans.

Monitoring resource consumption and request patterns is also recommended to
detect abnormal activity.

1. Force HTTPS:
   ```bash
   scalingo --app my-clamav-api force-https --enable
   ```

2. Add a rule to restrict access to the API to the specified IP range:
   ```bash
   scalingo --app my-clamav-api app-firewall-rule-add --cidr 203.0.113.42/28 --label "Access from Paris Office"
   ```

[clamav-tutorial]: https://doc.scalingo.com/tutorials/clamav
[application-firewall]: https://doc.scalingo.com/platform/networking/public/application-firewall
[force-https]: https://doc.scalingo.com/platform/networking/public/cert/force-https
[eicar]: https://www.eicar.org/

