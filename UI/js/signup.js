document.getElementById('signUp').addEventListener('submit', postData);
const appUrl = 'http://127.0.0.1:5000/v1/auth/signup';

/*
function returns success message 
*/

function outputSuccess() {
    output = 'Account Successfully created <br> <p class="center_text">You can now <a href="index.html">Login.</a></p>';
    document.getElementById('divSignup').innerHTML = output;
}


function postData(event) {
    event.preventDefault();

    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let role = 'True';

    fetch(appUrl, {
        method: 'POST',
        mode: 'cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name, email: email, password: password, role: role })
    }).then((res) => res.json())
        .then(outputSuccess())
        .catch((err) => console.log(err))
}
