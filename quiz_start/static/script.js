 const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            questions: [],
            currentIndex: 0,
            selectedAnswers: [],
            personalityTrait: ''
        };
    },
    methods: {
        getQuestions() {
            fetch(`/api/get-quiz/`)
                .then(response => response.json())
                .then(result => {
                    this.questions = result.data;
                });
        },
        selectAnswer(uid) {
            // console.log('Selected answer UID:', uid);
            this.selectedAnswers[this.currentIndex] = uid;
//            validateForm();
        },
        nextQuestion(event) {
            if (validateForm()) {
                // Proceed to next question
                event.preventDefault();
                this.currentIndex++;
                if (this.currentIndex == this.questions.length - 1) {
                    document.getElementById('next').style.display = 'none';
                    document.getElementById('submit').style.display = 'inline-block';
                }
            }
        },
        prevQuestion() {
            this.currentIndex--;
        },
        submitQuiz() {
            if (validateForm()) {
                // Proceed to quiz submission
                this.currentIndex++;
                fetch('/submit-quiz/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ answers: this.selectedAnswers })
                })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        alert('Failed to submit quiz. Please try again later.');
                    }
                })
                .then(data => {
    //                document.getElementById('submit').style.display = 'none';
    //                document.getElementById('quiz-question').style.display = 'none';
                    this.personalityTrait = data.personality_trait;
                    console.log('Personality Trait: ', this.personalityTrait);
                    document.querySelector('.result-image img').src = `/static/${this.personalityTrait}.png`;
                    document.getElementById('quiz-result').style.display = 'block';
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Failed to submit quiz. Please try again later.');
                });
            }
        }
    },
    created() {
        this.getQuestions();
    }
});

app.mount('#app');

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Function to validate the form
function validateForm() {
    const form = document.getElementById('quiz-form');
    if (form.checkValidity()) {
        return true;
    } else {
        return false;
    }
}

// window.addEventListener('load', function () {
//    // Check if the current page is not home.html
//    if (this.currentIdex > 0) {
//        prevQuestion();
//    }
//    if (window.location.pathname !== '') {
//        // Add an entry to the browser's history stack
//        window.history.pushState({ page: 'question' }, '', window.location.href);
//    }
//
//    // Listen for the popstate event (triggered when the user navigates back or forward)
//    window.addEventListener('popstate', function (event) {
//        if this.cu
//        // Check if the current page is home.html
//        if (window.location.pathname === '') {
//            // If the current page is home.html, navigate back one step in the history stack
//            window.history.go(-1);
//        }
//    });
//});


