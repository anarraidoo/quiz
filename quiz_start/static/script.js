 const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            questions: [],
            currentIndex: 0,
            selectedAnswers: []
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
        },
        nextQuestion() {
            this.currentIndex++;
        },
        submitQuiz() {
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
                // console.log('Selected answers:', this.selectedAnswers);
                const personalityTrait = data.personality_trait;
                // console.log('Personality Trait: ', personalityTrait);
                alert('Quiz submitted successfully! Personality Trait: ' + personalityTrait);
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Failed to submit quiz. Please try again later.');
            });
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