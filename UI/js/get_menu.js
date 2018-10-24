const appUrl = 'https://arty-fast.herokuapp.com/v1/'
let jwt = sessionStorage.getItem('jwt')

/*
function returns success message 
*/  
function outputSuccess(response) {
        let output = ''
        for(let x in response){ 
                console.log(response[x][0])
                output = output + `<div class="food_item">
                <div class="row">
                        <div class="col-2">
                            <h3>${response[x][0].name}</h3>
                        </div>
                        <div class="col-2">
                            <h3>Pricing : ${response[x][0].price}/=</h3>
                        </div>
                    </div>
                <p>${response[x][0].description}</p>
                    <input type="number" id="${response[x][0].menu_id}" placeholder="0" class="form_input_black" min="1"> 
                    <button class="blue-btn" onclick="post_order(${response[x][0].menu_id})">Click</button>
            </div>`
            }
        document.getElementById('food_menu').innerHTML = output;
}

/*
method to get menu
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
        .then((response) => outputSuccess(response))
        .catch((err) => console.log(err)) 
}
/*
method to output order success
*/
function order_success(response){
        console.log(response)
        output = ` <p class="info-success">
        <span>Message: </span> <br>
        ${response['msg']} <br>
        Refresh page to make another order.
        </p>`
        document.getElementById('food_menu').innerHTML = output;
}
/*
method to add food item to menu
*/
function post_order(x){
        console.log("Post order method called")
        console.log(x)
        let quantity = Number(document.getElementById(`${x}`).value)
        console.log(quantity)

        fetch(appUrl + 'users/orders', {
            method: 'POST',
            mode: 'cors',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization':`Bearer ${jwt}`
             },
            body: JSON.stringify({menu_id: x, quantity: quantity })
        }).then((res) => res.json())
            .then((response) => order_success(response))
            .catch((err) => console.log(err)) 
    }
