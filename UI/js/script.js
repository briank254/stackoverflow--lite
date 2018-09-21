// show alerts to users

const displayAlert = (message) => {
    const alertDiv = document.getElementById('alert-message');
    alertDiv.style.display = 'block';
    alertDiv.innerHTML = message;
};
