from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from orders.forms import RegistrationForm
from django.urls import reverse

from .models import Pizza

# Create your views here.
def index(request):
    context = {
        "pizzas": Pizza.objects.all()
    }
    return render(request, "orders/index.html", context)

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