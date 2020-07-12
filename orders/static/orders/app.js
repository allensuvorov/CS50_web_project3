document.addEventListener('DOMContentLoaded', () =>{
    console.log("on page load event");
    
    // run on load
    get_pizza_price();
    get_sub_price();
    get_dinner_platter_price();

    // grab the forms
    const pizza_form=document.forms.pizza_form;
    const sub_form=document.forms.sub_form;
    const dinner_platter_form=document.forms.dinner_platter_form;
    
    // set these listeners onto these forms 
    pizza_form.addEventListener('change', get_pizza_price);
    sub_form.addEventListener('change', get_sub_price);
    dinner_platter_form.addEventListener('change', get_dinner_platter_price);
      
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

function get_pizza_price() {
    
    // console.log("get pizza price event");
    let count = count_selected_toppings();
    // console.log('number of selected toppings = ' + count);

    // get data from user selection
    const pizza_size = document.getElementById('pizza_size').value;
    // const pizza_topping_combo = document.getElementById('pizza_topping_combo').value;
    const pizza_name = document.getElementById('pizza_name').value;
    
    // Initialize new AJAX request
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
    // console.log(pizza_name);

    request.send();
};

function get_add_ons_price_total(){

    let options = sub_add_on.options; // get all options 
    let total = 0;
        for (let i=0; i<options.length; i++) {
            if (options[i].selected) {
                
                total = total + parseFloat(options[i].dataset.price);

            };
        };
        return(total);
};

function get_sub_price() {
    console.log("getting sub price");
    let add_ons_price_total = get_add_ons_price_total();

    // get data from user selection
    const sub_name = document.getElementById('sub_name').value;
    const sub_size = document.getElementById('sub_size').value;

    // Initialize new AJAX request
    const request = new XMLHttpRequest();

    let URL = "sub_price?" + "sub_name=" + sub_name + "&sub_size=" + sub_size;
    // send AJAX request
    request.open('GET', URL, true);
    
    // Callback function for when request completes
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        console.log(data.price);
        if (data.price) {
            console.log(typeof(data.price));
            let total_sub_price = (parseFloat(data.price)+add_ons_price_total).toFixed(2);
            document.querySelector('#sub_price').innerHTML = total_sub_price+"$";
        }
        else {
            document.querySelector('#sub_price').innerHTML = "00.00$";
        };

    };
    // console.log(pizza_name);

    request.send();


};

function get_dinner_platter_price() {

};