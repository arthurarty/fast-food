const appUrl = 'http://127.0.0.1:5000/v1/'
let jwt = sessionStorage.getItem('jwt')
/*
function returns success message 
*/  
function outputSuccess(response) {
    let output = ''
    for(let x in response){ 
            console.log(response[x][0])
            output = output + ` <div class="order">
                    <strong>Order No: <i>${response[x][0].order_id}</i></strong> 
                    | menu_id : <i>${response[x][0].menu_id}</i><br>
                    Quantity : <i>${response[x][0].quantity}</i> 
                    | Status: <i>${response[x][0].status}</i> 
                    | User_id: <i>${response[x][0].user_id}</i>
                    | created_at : <i>${response[x][0].created_at}</i> <br>
                    <div class="btn-group">
                        <a href="" class="green-btn">View order</a>
                    </div>    
                </div>`
        }
    document.getElementById('orders').innerHTML = output;
}

/*
method to get orders
*/
function get_orders(){
    console.log("Add food method called")
    console.log(jwt)
    fetch(appUrl + 'orders', {
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