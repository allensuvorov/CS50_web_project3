from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
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
        form = UserCreationForm(request.POST)
        print (form.errors)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("index"))
            # return redirect("index")
            # TestMe1000me
        else:
            return render(request, "orders/register.html")
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, "orders/register.html", context)