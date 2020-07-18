# Project3 - "Pizza" (Django, JavaScript, AJAX, SQLite)
- Description: web application for handling a pizza restaurant’s online orders
- Video overview of the completed project: https://youtu.be/vHbjx0FEfRw 
- Project Spec: https://docs.cs50.net/ocw/web/projects/3/project3.html
- Course: CS50's Web Programming with Python and JavaScript


## Code Notes:

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
        - Index: main page, with total price calculation for the shopping cart
        - Auth: reg, login, logout
        - AJAX: to automatically get prices from the server for pizzas, subs and dinner platters
        - Cart: creates a cart record (in the order model) and adds selected item to the cart
        - Order: basically changes the status of the order from "Cart" to "Order" 
- static/orders/app.js
    - functions that get prices for pizzas, subs and dinner platters, as user changes any selection in the menu
- templates/orders/
    - base.html: HTML layout template
    - user.html: is the main user page with menu, cart and orders (pending and delivered)
- urls.py
    - contains paths and views (functions) triggered

## Other Notes:

### Insights:
- Order history needs absolute values, not links to values in ther tables, cause with time menu items get modified and deleted. But for simplicity, in this project we are using relation DB for order history. 
- Admin needs the list of all combinations to add a price to each of them.
- Reasons to create tables for each pizza option (types, sizes, toppings options): 1) to be able to display them on the menu section, using less space.

## Requirements

-Menu: Your web application should support all of the available menu items for Pinnochio’s Pizza & Subs (a popular pizza place in Cambridge). It’s up to you, based on analyzing the menu and the various types of possible ordered items (small vs. large, toppings, additions, etc.) to decide how to construct your models to best represent the information. Add your models to orders/models.py, make the necessary migration files, and apply those migrations.
Adding Items: Using Django Admin, site administrators (restaurant owners) should be able to add, update, and remove items on the menu. Add all of the items from the Pinnochio’s menu into your database using either the Admin UI or by running Python commands in Django’s shell.
Registration, Login, Logout: Site users (customers) should be able to register for your web application with a username, password, first name, last name, and email address. Customers should then be able to log in and log out of your website.
Shopping Cart: Once logged in, users should see a representation of the restaurant’s menu, where they can add items (along with toppings or extras, if appropriate) to their virtual “shopping cart.” The contents of the shopping should be saved even if a user closes the window, or logs out and logs back in again.
Placing an Order: Once there is at least one item in a user’s shopping cart, they should be able to place an order, whereby the user is asked to confirm the items in the shopping cart, and the total (no need to worry about tax!) before placing an order.
Viewing Orders: Site administrators should have access to a page where they can view any orders that have already been placed.
Personal Touch: Add at least one additional feature of your choosing to the web application. Possibilities include: allowing site administrators to mark orders as complete and allowing users to see the status of their pending or completed orders, integrating with the Stripe API to allow users to actually use a credit card to make a purchase during checkout, or supporting sending users a confirmation email once their purchase is complete. If you need to use any credentials (like passwords or API credentials) for your personal touch, be sure not to store any credentials in your source code, better to use environment variables!
In README.md, include a short writeup describing your project, what’s contained in each file you created or modified, and (optionally) any other additional information the staff should know about your project. Also, include a description of your personal touch and what you chose to add to the project.
If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!
Beyond these requirements, the design, look, and feel of the website are up to you! You’re also welcome to add additional features to your website, so long as you meet the requirements laid out in the above specification!
