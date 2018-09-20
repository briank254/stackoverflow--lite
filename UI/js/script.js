// show alerts to users

let displayAlert = (message) => {
    let alertDiv = document.getElementById("alert-message");
    alertDiv.style.display = "block";
    alertDiv.innerHTML = message;

}