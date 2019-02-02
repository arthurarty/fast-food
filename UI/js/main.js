document.getElementById('signin').addEventListener('submit', signin);
const appUrl = 'http://127.0.0.1:5000/v1/'
let jwt = ''

/*
function returns success message 
*/
function outputSuccess(response) {
        if (response['msg'] == undefined){
            output = 'Login successful. <br> <p class="center_text">You can now <a href="view_menu.html">View menu.</a></p>'
            document.getElementById('divSignup').innerHTML = output;
            jwt = response[1]['access_token']
            sessionStorage.setItem('jwt', jwt);
            console.log(jwt)
        }
        else {
            output = `Login unsuccessful. <br>  ${response['msg']}`
            document.getElementById('divSignup').innerHTML = output;
            console.log(response['msg'])
        }
        //setTimeout(window.location.replace("view_menu.html"), 9000)
}

/*
post email and password
*/
function signin(event) {
    event.preventDefault()
    console.log("signin method called")

    let email = document.getElementById('email').value
    let password = document.getElementById('password').value

    fetch(appUrl + 'auth/login', {
        method: 'POST',
        mode: 'cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({email: email, password: password })
    }).then((res) => res.json())
        .then((response) => outputSuccess(response))
        .catch((err) => console.log(err))
}
