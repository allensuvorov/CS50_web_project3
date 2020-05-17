from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from orders.forms import RegistrationForm
from django.urls import reverse

from .models import Pizza, Pizza_name, Pizza_size, Pizza_topping

# Create your views here.
def index(request):
    # if user is not authenticated than show index page with login and register links
    if not request.user.is_authenticated:
        return render(request, "orders/index.html", {"message": None})
    
    # else show user page
    
    context = {
        "pizzas": Pizza.objects.all(),
        "pizza_names": Pizza_name.objects.all(),
        "pizza_sizes": Pizza_size.objects.all(),
        "pizza_toppings": Pizza_topping.objects.all(),
        
        "user": request.user
    }
    return render(request, "orders/user.html", context)

def register_view(request):
    
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        print (form.errors)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "orders/register.html")
    else:
        form = RegistrationForm()
        context = {
            "form": form
        }
        return render(request, "orders/register.html", context)

def login_view(request):
    if request.method =='POST':

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "orders/login.html", {"message": "Enter credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/index.html", {"message": "Logged out."})

# def add_view(request):
#     try: