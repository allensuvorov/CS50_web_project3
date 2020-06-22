document.addEventListener('DOMContentLoaded', () =>{
    console.log("on page load event");
    get_price();
    // const pizza_form=document.querySelector('#pizza_form');
    const pizza_form=document.forms.pizza_form;
    const pizza_toppings=document.getElementById('pizza_toppings');
    // console.log(pizza_toppings.value);

    pizza_toppings.addEventListener('change', set_topping_combo);
    pizza_form.addEventListener('change', get_price);
      
});

function set_topping_combo() {

    let options = pizza_toppings.options;
    let count = 0;
    for (let i=0; i<options.length; i++) {
        if (options[i].selected) {
            count++;
        };
    };

    // console.log('number of selected toppings = ' + count);
    
    document.querySelector('#pizza_topping_combo_selected').innerHTML = count + " toppings";
    
};

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
        if (data.price) {

            document.querySelector('#pizza_price').innerHTML = data.price+"$";
        }
        else {
            document.querySelector('#pizza_price').innerHTML = "00.00$";
        };

    };
    

    console.log(pizza_name);

    request.send();
};