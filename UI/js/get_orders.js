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
                        <button class="green-btn" onclick="get_single_order(${response[x][0].order_id})">
                        View order
                        </button>
                    </div>    
                </div>`
        }
    document.getElementById('orders').innerHTML = output;
}

/*
method to get orders
*/
function get_orders(){
    console.log("Get order method called")
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

/*
out put a single order
*/
function output_single_order(response){
    console.log(response[0])
    let output = ` <div class="order">
                    <strong>Order No: <i>${response[0].order_id}</i></strong><br>
                    Menu_id : <i>${response[0].menu_id}</i><br>
                    Quantity : <i>${response[0].quantity}</i> <br>
                    Status: <i>${response[0].status}</i> <br>
                    User_id: <i>${response[0].user_id}</i><br>
                    Created_at : <i>${response[0].created_at}</i> <br>
                    <select class="form_input_select" id="status">
                    <option value="Complete">Complete</option>
                    <option value="Processing">Processing</option>
                    <option value="Cancelled">Cancelled</option>
                    </select>
                    <div class="btn-group row">
                    <button class="blue-btn col-2" onclick="update_status(${response[0].order_id})">
                    Update order
                    </button>
                    <button class="green-btn col-2" onclick="get_orders()">
                    View all orders
                    </button>
                    </div> 
                </div>`
    document.getElementById('orders').innerHTML = output
}

/*
method returns a single order
*/
function get_single_order(order_id){
    console.log("Get single order method called")
    console.log(jwt)
    fetch(appUrl + `orders/${order_id}`, {
        method: 'GET',
        mode: 'cors',
        headers: { 
            'Content-Type': 'application/json',
            'Authorization':`Bearer ${jwt}`
         }
}).then((res) => res.json())
        .then((response) => output_single_order(response))
        .catch((err) => console.log(err)) 
}

/*
method to show update success. 
*/
function update_success(response){
    console.log(response)
    output = ` <p class="info-success">
    <span>Message: </span> <br>
    ${response['msg']} <br>
    Refresh page to make another order.
    </p>
    <button class="green-btn col-2" onclick="get_orders()">
    View all orders
    </button>`
    document.getElementById('orders').innerHTML = output;
}

/*
function to update status
*/
function update_status(order_id){
    console.log("Update status method")
    let status = document.getElementById(`status`).value
    fetch(appUrl + `orders/${order_id}/`, {
        method: 'PUT',
        mode: 'cors',
        headers: { 
            'Content-Type': 'application/json',
            'Authorization':`Bearer ${jwt}`
         },
        body: JSON.stringify({status: status })
    }).then((res) => res.json())
        .then((response) => update_success(response))
        .catch((err) => console.log(err)) 
}
