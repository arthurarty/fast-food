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
                <form class="quantity_form" action="confirm_order.html" method="get">
                    <input type="number" name="quantity" placeholder="0" class="form_input" min="1"> 
                    <input type="submit" class="blue-btn" value="Order">
                </form>
            </div>`
            }
        document.getElementById('food_menu').innerHTML = output;
        //console.log(response)

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