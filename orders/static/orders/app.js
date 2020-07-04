document.addEventListener('DOMContentLoaded', () =>{
    console.log("on page load event");
    get_price();
    // const pizza_form=document.querySelector('#pizza_form');
    const pizza_form=document.forms.pizza_form;
    
    const pizza_toppings=document.getElementById('pizza_toppings');
    // console.log(pizza_toppings.value);
    
    pizza_form.addEventListener('change', get_price);
      
});

function count_selected_toppings() {

    let options = pizza_toppings.options;
    let count = 0;
    for (let i=0; i<options.length; i++) {
        if (options[i].selected) {
            count++;
        };
    };

    // document.querySelector('#pizza_topping_combo_selected').innerHTML = count + " toppings";
    
    // if count is higher than 4, then just return 4
    if (count>4) {
        count = 4;
    };
    
    return (count);
};

function get_price() {
    
    console.log("get price event");
    let count = count_selected_toppings();
    console.log('number of selected toppings = ' + count);

    // get data from user selection
    const pizza_size = document.getElementById('pizza_size').value;
    // const pizza_topping_combo = document.getElementById('pizza_topping_combo').value;
    const pizza_name = document.getElementById('pizza_name').value;
    
    // Initialize new request
    const request = new XMLHttpRequest();

    let URL = "price?" + "pizza_name=" + pizza_name + "&pizza_size=" + pizza_size + "&toppings_count=" + count;
    request.open('GET', URL, true);

    // Callback function for when request completes
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        console.log(data.price);
        if (data.price) {

            document.querySelector('#pizza_price').innerHTML = data.price+"$";
        }
        else {
            document.querySelector('#pizza_price').innerHTML = "00.00$";
        };

        if (data.combo) {
            
            const combo = document.querySelector('#pizza_topping_combo')
            combo.innerHTML = data.combo;
            combo.setAttribute("value", data.combo_id)

        };

    };
    

    console.log(pizza_name);

    request.send();
};