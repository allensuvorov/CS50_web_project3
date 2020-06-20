document.addEventListener('DOMContentLoaded', () =>{
    console.log("on page load event");
    const pizza_form=document.querySelector('#pizza_form');
    pizza_form.addEventListener('change', get_price);
      
});

function get_price() {
    
    console.log("pizza_form change event");
    
};