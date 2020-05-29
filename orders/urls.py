from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # Links to Login page and Register page, if signed in - redirect to user page
    path("register", views.register_view, name ="register"), # reg form, once registered - to login page, other - to error page
    path("login", views.login_view, name="login"), # login form, once signed-in - to index, other - to login page with error
    path("logout", views.logout_view, name="logout"), # to login page with message "logged out"
    path("add", views.add_view, name="add") # to add an item to shopping cart
]
