const appUrl = 'http://127.0.0.1:5000/v1/'
let jwt = sessionStorage.getItem('jwt')

/*
function returns success message 
*/  
function outputSuccess(response) {
        let output = ''
        for(let x in response){ 
                console.log(response[x][0].description)
            }
        //document.getElementById('food_menu').innerHTML = output;
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