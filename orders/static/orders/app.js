document.addEventListener('DOMContentLoaded', () =>{
    console.log("on page load event");
    get_price();
    // const pizza_form=document.querySelector('#pizza_form');
    const pizza_form=document.forms.pizza_form;

    pizza_form.addEventListener('change', get_price);
      
});

function get_price() {
    
    console.log("get price event");
    
    // get data from user selection
    const pizza_size = document.getElementById('pizza_size').value;
    const pizza_topping_combo = document.getElementById('pizza_topping_combo').value;
    const pizza_name = document.getElementById('pizza_name').value;

    // Initialize new request
    const request = new XMLHttpRequest();

    let URL = "price?" + "pizza_name=" + pizza_name + "&pizza_topping_combo=" + pizza_topping_combo +"&pizza_size=" + pizza_size
    request.open('GET', URL, true)

    // Callback function for when request completes
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        console.log(data.price)
        document.querySelector('#pizza_price').innerHTML = data.price;
    }
    

    console.log(pizza_name);

    request.send();
};