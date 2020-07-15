# Project3 - Pizza

- Course: Web Programming with Python and JavaScript
- Project Spec: https://docs.cs50.net/ocw/web/projects/3/project3.html

## Code:

- models.py: 
    - contains all DB tables for the project
- forms.py:
    - contains setup of an extended registration form: 
        - creates `RegistrationForm` class, that is based on `UserCreationForm` class built into Django.
- admin.py:
    - models are added here to show them in admin site
    - inline classes added to show related models in admin site (order items in each order)
- views.py:
    - Setup: importing classes, models
    - Functions:
        - Index - main page
        - Auth region: reg, login, logout
        - AJAX: to automatically get prices from the server for pizzas, subs and dinner platters
        - Cart: creates a cart record (in the order model) and adds selected item to the cart
        - Order: basically changes the status of the order from "Cart" to "Order" 
- static/orders/app.js
    - functions that get prices for pizzas, subs and dinner platters, as user changes any selection in the menu
- templates/order/
    - base.html: HTML layout template
    - user.html: is the main user page with menu, cart and orders (pending and delivered)
- urls.py
    - contains paths and views (functions) triggered

## Notes:

### Models: ()
- order

### Insights:
- Order history needs absolute values, not links to values in ther tables, cause items get modified and deleted.
- Admin needs the list of all combinations to add a price to each of them.
- Reasons to create tables for each pizza option (types, sizes, toppings options): 1) to be able to display them on the menu. 

### Presentation data
- username: JonSmith
- password: supertest5544
- email: 55test@test.com