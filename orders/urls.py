from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # Links to Login page and Register page, if signed in - redirect to user page
    path("register", views.register_view, name ="register"), # reg form, once registered - to login page, other - to error page
    path("login", views.login_view, name="login"), # login form, once signed-in - to index, other - to login page with error
    path("logout", views.logout_view, name="logout"), # to login page with message "logged out"
    
    path("pizza_price", views.pizza_price_view, name="pizza_price"), # for getting pizza price via AJAX
    path("sub_price", views.sub_price_view, name="sub_price"), # getting sub price via AJAX
    path("dinner_platter_price", views.dinner_platter_price_view, name="dinner_platter_price"), # getting dinner platter price via AJAX
    
    path("cart_pizza", views.cart_pizza_view, name="cart_pizza"), # to add a pizza order item to shopping cart
    path("cart_sub", views.cart_sub_view, name="cart_sub"), # add sub item to cart
    path("cart_dinner_platter", views.cart_dinner_platter_view, name="cart_dinner_platter"),
    path("cart_pasta", views.cart_pasta_view, name="cart_pasta"),
    path("cart_salad", views.cart_salad_view, name="cart_salad"),
    
    path("<int:order_id>/order", views.order_view, name ="order") # for placing an order
]
