document.getElementById('food_add').addEventListener('submit', add_food)
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
function add_food(event){
    event.preventDefault()
    console.log("Add food method called")
    console.log(jwt)

    let desc = document.getElementById('desc').value
    let food_name = document.getElementById('food_name').value
    let price = Number(document.getElementById('price').value)

    console.log(price)
    fetch(appUrl + 'menu', {
        method: 'POST',
        mode: 'cors',
        headers: { 
            'Content-Type': 'application/json',
            'Authorization':`Bearer ${jwt}`
         },
        body: JSON.stringify({food_name: food_name, price: price, desc:desc })
    }).then((res) => res.json())
        .then((response) => outputSuccess(response))
        .catch((err) => console.log(err)) 
}