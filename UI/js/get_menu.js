const appUrl = 'http://127.0.0.1:5000/v1/'
let jwt = sessionStorage.getItem('jwt')

/*
function returns success message 
*/  
function outputSuccess(response) {
        output = ` <p class="info-success">
        <span>Message: </span> <br>
        ${response['msg']} <br>
        Refresh page to add another item.
        </p>`
        document.getElementById('food_menu').innerHTML = output;
        console.log(response)
}

/*
method to add food item to menu
*/
function get_menu(){
    console.log("Add food method called")
    console.log(jwt)
    fetch(appUrl + 'menu', {
        method: 'GET',
        mode: 'cors',
        headers: { 
            'Content-Type': 'application/json',
            'Authorization':`Bearer ${jwt}`
         }
}).then((res) => res.json())
        .then((response) => console.log(response))
        .catch((err) => console.log(err)) 
}