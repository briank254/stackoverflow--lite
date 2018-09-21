const signup = (event) => {
    event.preventDefault();
    const form = event.target;
    const data = {};
    data.first_name = form.firstname.value;
    data.last_name = form.lastname.value;
    data.email = form.email.value;
    data.password = form.password.value;
    data.confirm_password = form.confirmpassword.value;

    fetch('http://127.0.0.1:5000/api/v2/auth/signup', {
        method: 'POST',
        headers: { 'Content-type': 'application/json' },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then((data) => {
            if (data.message === 'Please fill in all fields') {
                displayAlert('Please fill in all fields');
            }
            if (data.message === 'Invalid Email') {
                displayAlert('Input email in the format example@example.com');
            }
            if (data.message === 'Password too short') {
                displayAlert('Password should have more than 8 characters');
            }
            if (data.message === 'Passwords do not match') {
                displayAlert('Passwords do not match');
            }

            if (data.message === 'user already exists') {
                displayAlert('user already exists');
            }
            if (data.message === 'Account created') {
                window.location.replace('index.html');
            }
        })
        .catch(error => (error));
};

const signupform = document.getElementById('signup-form');
if (signupform) {
    signupform.addEventListener('submit', signup);
}
const signin = () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const data = {
        email, password,
    };


    fetch('http://127.0.0.1:5000/api/v2/auth/signin', {
        method: 'POST',
        headers: { 'Content-type': 'application/json' },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then((data) => {
            if (data.message === 'Missing email parameter') {
                displayAlert('Missing email parameter');
            }
            if (data.message === 'Missing password parameter') {
                displayAlert('Missing password parameter');
            }
            if (data.message === 'Invalid email or password') {
                displayAlert('Invalid email or password');
            }

            if (data.success === 'Signin successful') {
                window.location.replace('questions.html');
                localStorage.setItem('access_token', data.access_token);
            }
        })
        .catch(error => (error));
};

const getQuestions = () => {
    fetch('http://127.0.0.1:5000/api/v2/questions', {
        method: 'GET',
        headers: { 'Content-type': 'application/json' },

    })
        .then(response => response.json())
        .then(data => {
            const { questions } = data;
            let output = '';

            for (let counter = 0; counter < questions.length; counter++) {
                const questionId = questions[counter].id;
                const { author } = questions[counter];
                const { title } = questions[counter];
                const { question } = questions[counter];

                output += `<div class='que-body' data-id=${questionId}>
                <div class='que-wrapper' >
                <h3 id='title' data-id=${questionId}>
                    <a href='answers.html' data-id=${questionId}>${title} </a>
                </h3>
                <h4 id='question' data-id=${questionId}>
                    <a href='answers.html' style='color:black;'>${question}</a>
                </h4>
                <h5> 
                Author : ${author}
                </h5>
                </div>
                </div>`;
            }
            document.getElementById('question').innerHTML = output;
            const div = document.getElementsByClassName('que-body');
            for (let i = 0; i < div.length; i++) {
                div[i].addEventListener('click', getQuestion)
            }
        })
        .catch(error => (error));
};

const postQuestion = (e) => {
    e.preventDefault();
    const form = e.target;
    const data = {};
    data.title = form.title.value;
    data.question = form.question.value;

    fetch('http://127.0.0.1:5000/api/v2/questions', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('access_token')}`
        },
        body: JSON.stringify(data),

    })
        .then(res => res.json())
        .then((data) => {
            if (data.message === 'Please fill in all fields') {
                displayAlert('Please fill in all fields');
            }
            if (data.error === 'A question with this title exists') {
                displayAlert('A question with this title exists');
            }
            if (data.message === 'question posted') {
                window.location.replace('questions.html');
                localStorage.setItem('access_token', data.access_token);
            }
        })
        .catch(error => (error));
};
const questionForm = document.getElementById('question-form');
if (questionForm) {
    questionForm.addEventListener('submit', postQuestion);
}

const getQuestion = (event) => {
    const token = localStorage.getItem('access_token');
    const question = event.target;
    const questionId = question.getAttribute('data-id');
    const url = `http://127.0.0.1:5000/api/v2/questions/${questionId}`;

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-type': 'application/json',
            Authorization: `'Bearer ' ${token}`
        },
    })
        .then(response => response.json())
        .then((data) => {
            localStorage.setItem('specific_qn', data.question.question);
            localStorage.setItem('qn_id', data.question.id);
            location.href = 'answers.html';
        })
        .catch(error => (error));
};

const postAnswer = (event) => {
    event.preventDefault();
    const form = event.target;
    const data = {};
    data.answer = form.answer.value;
    const token = localStorage.getItem('access_token');
    const questionId = localStorage.getItem('qn_id');

    const url = `http://127.0.0.1:5000/api/v2/questions/${questionId}/answers`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            Authorization: `'Bearer ' ${token}`
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then((data) => {
            if (data.message === 'You cannot answer your own question') {
                displayAlert('You cannot answer your own question');
            }
            if (data.message === 'You have successfully answered the question') {
                setTimeout(function () { location.reload(true); }, 1000);
            }
        })
        .catch(error => (error));
};
const answerForm = document.getElementById('answer-form');
if (answerForm) {
    answerForm.addEventListener('submit', postAnswer);
}

if (window.location.pathname.endsWith('answers.html')) {
    const token = localStorage.getItem('access_token');
    const questionId = localStorage.getItem('qn_id');
    fetch(`http://127.0.0.1:5000/api/v2/questions/${questionId}/answers`, {
        method: 'GET',
        headers: {
            'Content-type': 'application/json',
            Authorization: `'Bearer ' ${token}`
        },

    })
        .then(response => response.json())
        .then((data) => {
            const { answers } = data;
            let output = '';
            for (let counter = 0; counter < answers.length; counter++) {
                const answerId = answers[counter].id;
                const userName = answers[counter].user_name;
                const { answer } = answers[counter];

                output += `
                <div class="que-body">
                    <div class="que-wrapper">
                        <p> ${answer}
                        </p>
                    </div>
                </div>
    
                `;
            }
            document.getElementById('ans').innerHTML = output;
        })
        .catch(error => (error));
}
