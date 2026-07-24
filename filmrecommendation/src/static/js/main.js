// Main JavaScript for Film Recommendations

// Utility functions
const utils = {
    // Debounce function for input validation
    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    // Image loading with fallback
    loadImageWithFallback: (imageElement, imageUrl, fallbackUrl) => {
        const img = new Image();
        img.onload = () => {
            imageElement.src = imageUrl;
            imageElement.classList.add('loaded');
        };
        img.onerror = () => {
            imageElement.src = fallbackUrl;
            imageElement.classList.add('film-placeholder');
        };
        img.src = imageUrl;
    },

    // Show notification
    showNotification: (message, type = 'info') => {
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
            type === 'error' ? 'bg-red-500 text-white' : 
            type === 'success' ? 'bg-green-500 text-white' : 
            'bg-blue-500 text-white'
        }`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            notification.remove();
        }, 5000);
    },

    // Format text for display
    formatText: (text, maxLength = 200) => {
        if (text.length <= maxLength) return text;
        return text.substring(0, maxLength) + '...';
    }
};

// Form validation
const formValidator = {
    validateQuery: (query) => {
        return query.trim().length >= 10;
    },

    showValidationError: (message) => {
        const errorElement = document.getElementById('validationMessage');
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.classList.remove('hidden');
        }
    },

    hideValidationError: () => {
        const errorElement = document.getElementById('validationMessage');
        if (errorElement) {
            errorElement.classList.add('hidden');
        }
    }
};

// API service
const apiService = {
    baseURL: window.location.origin,
    
    async getRecommendations(query, k = 3) {
        try {
            const response = await fetch(`${this.baseURL}/recommendations`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query, k })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Server error');
            }

            return await response.json();
        } catch (error) {
            throw new Error(error.message || 'Connection error');
        }
    },

    async healthCheck() {
        try {
            const response = await fetch(`${this.baseURL}/health`);
            return await response.json();
        } catch (error) {
            throw new Error('Service unavailable');
        }
    }
};

// UI state manager
const uiState = {
    setLoading: (isLoading) => {
        const submitBtn = document.getElementById('submitBtn');
        const btnText = document.getElementById('btnText');
        const loadingText = document.getElementById('loadingText');
        
        if (submitBtn && btnText && loadingText) {
            submitBtn.disabled = isLoading;
            btnText.classList.toggle('hidden', isLoading);
            loadingText.classList.toggle('hidden', !isLoading);
        }
    },

    showResults: (results) => {
        const resultsSection = document.getElementById('resultsSection');
        const resultsContainer = document.getElementById('resultsContainer');
        
        if (resultsSection && resultsContainer) {
            resultsContainer.innerHTML = '';
            
            results.forEach((film, index) => {
                const filmCard = uiState.createFilmCard(film, index + 1);
                resultsContainer.appendChild(filmCard);
            });
            
            resultsSection.classList.remove('hidden');
            resultsSection.scrollIntoView({ behavior: 'smooth' });
        }
    },

    showError: (message) => {
        const errorSection = document.getElementById('errorSection');
        const errorMessage = document.getElementById('errorMessage');
        
        if (errorSection && errorMessage) {
            errorMessage.textContent = message;
            errorSection.classList.remove('hidden');
            errorSection.scrollIntoView({ behavior: 'smooth' });
        }
    },

    hideError: () => {
        const errorSection = document.getElementById('errorSection');
        if (errorSection) {
            errorSection.classList.add('hidden');
        }
    },

    createFilmCard: (film, index) => {
        const card = document.createElement('div');
        card.className = 'film-card fade-in';
        card.style.animationDelay = `${index * 0.1}s`;
        
        // Image with fallback
        const imageUrl = film.image_url || '/static/images/film-placeholder.svg';
        const fallbackUrl = '/static/images/film-placeholder.svg';
        const imageAlt = `Poster for the film ${film.title}`;
        
        card.innerHTML = `
            <div class="flex items-start space-x-3 sm:space-x-4">
                <div class="flex-shrink-0">
                    <div class="relative">
                        <img 
                            alt="${imageAlt}"
                            class="film-image w-16 h-20 sm:w-20 sm:h-28 object-cover rounded-lg shadow-md"
                            loading="lazy"
                        />
                        <div class="absolute -top-2 -right-2 w-6 h-6 sm:w-7 sm:h-7 bg-primary-500 rounded-full flex items-center justify-center text-white font-bold text-xs sm:text-sm shadow-lg">
                            ${index}
                        </div>
                    </div>
                </div>
                <div class="flex-1 min-w-0">
                    <h3 class="text-lg sm:text-xl font-bold text-gray-900 mb-2 break-words">${film.title}</h3>
                    <p class="text-sm sm:text-base text-gray-700 leading-relaxed break-words">${film.description}</p>
                </div>
            </div>
        `;
        
        // Load image with fallback
        const imgElement = card.querySelector('img');
        utils.loadImageWithFallback(imgElement, imageUrl, fallbackUrl);
        
        return card;
    }
};

// Event handlers
const eventHandlers = {
    init: () => {
        // Form submission
        const form = document.getElementById('searchForm');
        if (form) {
            form.addEventListener('submit', eventHandlers.handleFormSubmit);
        }

        // Example query buttons
        document.querySelectorAll('.example-query').forEach(button => {
            button.addEventListener('click', eventHandlers.handleExampleClick);
        });

        // Input validation
        const queryInput = document.getElementById('query');
        if (queryInput) {
            queryInput.addEventListener(
                'input', 
                utils.debounce(eventHandlers.handleInputChange, 300)
            );
        }

        // Mobile menu toggle
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');
        if (mobileMenuButton && mobileMenu) {
            mobileMenuButton.addEventListener('click', eventHandlers.toggleMobileMenu);
        }

        // Health check on page load
        eventHandlers.checkApiHealth();
    },

    handleFormSubmit: async (e) => {
        e.preventDefault();
        
        const queryInput = document.getElementById('query');
        const kSelect = document.getElementById('k');
        
        if (!queryInput || !kSelect) return;
        
        const query = queryInput.value.trim();
        const k = parseInt(kSelect.value);
        
        // Validation
        if (!formValidator.validateQuery(query)) {
            formValidator.showValidationError('Please enter at least 10 characters');
            return;
        }
        
        formValidator.hideValidationError();
        uiState.hideError();
        uiState.setLoading(true);
        
        try {
            const response = await apiService.getRecommendations(query, k);
            uiState.showResults(response.results);
            utils.showNotification('Recommendations found!', 'success');
        } catch (error) {
            uiState.showError(error.message);
            utils.showNotification('Error while searching', 'error');
        } finally {
            uiState.setLoading(false);
        }
    },

    handleExampleClick: (e) => {
        const queryInput = document.getElementById('query');
        if (queryInput) {
            const exampleText = e.target.textContent.trim().replace(/"/g, '');
            queryInput.value = exampleText;
            queryInput.focus();
            
            // Trigger validation
            eventHandlers.handleInputChange();
        }
    },

    handleInputChange: () => {
        const queryInput = document.getElementById('query');
        if (!queryInput) return;
        
        const isValid = formValidator.validateQuery(queryInput.value);
        
        if (queryInput.value.length > 0 && !isValid) {
            formValidator.showValidationError('Please enter at least 10 characters');
        } else {
            formValidator.hideValidationError();
        }
    },

    checkApiHealth: async () => {
        try {
            await apiService.healthCheck();
            console.log('API is healthy');
        } catch (error) {
            console.warn('API health check failed:', error.message);
            utils.showNotification('Service temporarily unavailable', 'error');
        }
    },

    toggleMobileMenu: () => {
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        
        if (mobileMenu && mobileMenuButton) {
            const isHidden = mobileMenu.classList.contains('hidden');
            
            if (isHidden) {
                mobileMenu.classList.remove('hidden');
                // Change icon to X
                mobileMenuButton.innerHTML = `
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                    </svg>
                `;
            } else {
                mobileMenu.classList.add('hidden');
                // Change icon back to hamburger
                mobileMenuButton.innerHTML = `
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                `;
            }
        }
    }
};

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', eventHandlers.init);

// Export for potential use in other scripts
window.FilmRecommendations = {
    utils,
    formValidator,
    apiService,
    uiState,
    eventHandlers
};
