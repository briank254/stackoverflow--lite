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
        .then((res) => res.json())

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

