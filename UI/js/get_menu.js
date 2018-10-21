const appUrl = 'http://127.0.0.1:5000/v1/'
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
                <form class="quantity_form" id='post_order'>
                    <input type="number" id="quantity" placeholder="0" class="form_input" min="1"> 
                    <input type="number" class="form_input_hide" id="menu_id" value="${response[x][0].menu_id}">
                    <input type="submit" class="blue-btn" value="Order">
                </form>
            </div>`
            }
        document.getElementById('food_menu').innerHTML = output;
        //console.log(response)
        document.getElementById('post_order').addEventListener('submit', post_order);
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
        .then((response) => outputSuccess(response))
        .catch((err) => console.log(err)) 
}

/*
method to add food item to menu
*/
function post_order(event){
        event.preventDefault()
        console.log("Post order method called")

        let menu_id = Number(document.getElementById('menu_id').value)
        let quantity = Number(document.getElementById('quantity').value)

        fetch(appUrl + 'users/orders', {
            method: 'POST',
            mode: 'cors',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization':`Bearer ${jwt}`
             },
            body: JSON.stringify({menu_id: menu_id, quantity: quantity })
        }).then((res) => res.json())
            .then((response) => console.log(response))
            .catch((err) => console.log(err)) 
    }
