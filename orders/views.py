# region Setup
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from orders.forms import RegistrationForm
from django.urls import reverse

from .models import Pizza, PizzaName, PizzaSize, PizzaTopping, PizzaToppingCombo, Order, OrderStatus, PizzaOrderItem, SubOrderItem, DinnerPlatterOrderItem, PastaOrderItem, SaladOrderItem, Sub, SubAddOn, SubName, SubSize, Pasta, Salad, DinnerPlatter, DinnerPlatterName, DinnerPlatterSize
# endregion Setup

# Create your views here.

def index(request):
    # if user is not authenticated than show index page with login and register links
    if not request.user.is_authenticated:
        return render(request, "orders/index.html", {"message": None})
    
    # else show user page
    
    # If cart exists, calculate total price for cart
    if Order.objects.filter(user=request.user, status=1).exists():
        cart = Order.objects.get(user=request.user, status=1)

        total_price = 0
        # print ("\n", total_price, "\n")
        

        if cart.pizzas.exists():
            cart_pizzas = cart.pizzas.all()
            print ("Pizzas")
            for item in cart_pizzas:
                order_item_price = item.pizza.price * item.count
                print (order_item_price)
                total_price += order_item_price

        if cart.subs.exists():
            cart_subs = cart.subs.all()
            print ("Subs")
            for item in cart_subs:
                add_ons = item.add_ons.all()
                add_ons_total_price = 0
                
                for add_on in add_ons:
                    add_ons_total_price +=add_on.price
                    # print (add_on.price)

                order_item_price = (item.sub.price+add_ons_total_price) * item.count
                
                print (order_item_price)
                total_price += order_item_price

        if cart.dinner_platters.exists():
            cart_dinner_platters = cart.dinner_platters.all()
            print ("DinnerPlatters")
            for item in cart_dinner_platters:
                order_item_price = item.dinner_platter.price * item.count
                print (order_item_price)
                total_price += order_item_price

        if cart.pastas.exists():
            cart_pastas = cart.pastas.all()
            print ("Pastas")
            for item in cart_pastas:
                order_item_price = item.pasta.price * item.count
                print (order_item_price)
                total_price += order_item_price

        if cart.salads.exists():
            cart_salads = cart.salads.all()
            print ("Salads")
            for item in cart_salads:
                order_item_price = item.salad.price * item.count
                print (order_item_price)
                total_price += order_item_price

        # save total price to current order
        cart.price = total_price
        cart.save()
        print ("\n","CART: ", cart, "\n")

    else:

        print ("\n","no cart", "\n")

    context = {
        "pizzas": Pizza.objects.all(),
        "pizza_names": PizzaName.objects.all(),
        "pizza_sizes": PizzaSize.objects.all(),
        "pizza_topping_combos": PizzaToppingCombo.objects.all(),
        "pizza_toppings": PizzaTopping.objects.all(),
        "cart": Order.objects.filter(user=request.user, status=1),
        "pending_orders": Order.objects.filter(user=request.user, status = 2),
        "delivered_orders": Order.objects.filter(user=request.user, status = 3),
        "user": request.user,
        "subs": Sub.objects.all(),
        "sub_names": SubName.objects.all(),
        "sub_sizes": SubSize.objects.all(),
        "sub_add_ons": SubAddOn.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "dinner_platters": DinnerPlatter.objects.all(),
        "dinner_platter_names": DinnerPlatterName.objects.all(),
        "dinner_platter_sizes": DinnerPlatterSize.objects.all()

    }
    return render(request, "orders/user.html", context)

# region Authentification views
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
#endregion Authentification

# region Price via AJAX views
def pizza_price_view(request):

    if request.is_ajax and request.method == "GET":
        # get data name from the client side
        pizza_name_id = int(request.GET["pizza_name"])
        pizza_size_id = int(request.GET["pizza_size"])
        
        # get number of toppings selected
        toppings_count = int(request.GET["toppings_count"])
        pizza_topping_combo = PizzaToppingCombo.objects.get(count=toppings_count)
        pizza_topping_combo_id = pizza_topping_combo.id

    try:
        pizza = Pizza.objects.get(name=pizza_name_id, size=pizza_size_id, combo=pizza_topping_combo_id)
        price = pizza.price
        combo = pizza_topping_combo.combo

    except Pizza.DoesNotExist:
        return JsonResponse ({'message': 'not in menu'})

    return JsonResponse ({
        'price': price,
        'combo': combo,
        'combo_id': pizza_topping_combo_id
        })

def sub_price_view(request):

    if request.is_ajax and request.method == "GET":
        
        # get data name from the client side.
        sub_name_id = int(request.GET["sub_name"])
        sub_size_id = int(request.GET["sub_size"])
    try:
        sub = Sub.objects.get(name=sub_name_id, size=sub_size_id)
        price = sub.price

    except Sub.DoesNotExist:
        return JsonResponse ({'message': 'not in menu'})

    return JsonResponse ({
        'price': price
        })

def dinner_platter_price_view(request):
    if request.is_ajax and request.method == "GET":
        dinner_platter_name_id = int(request.GET["dinner_platter_name"])
        dinner_platter_size_id = int(request.GET["dinner_platter_size"])
    try:
        dinner_platter = DinnerPlatter.objects.get(name=dinner_platter_name_id, size=dinner_platter_size_id)
        price = dinner_platter.price

    except DinnerPlatter.DoesNotExist:
        return JsonResponse ({'message': 'not in menu'})
    
    return JsonResponse ({
        'price': price
        })
#endregion Price via AJAX

# region Cart views
def cart_pizza_view(request):
    
    # add check if cart is already in created, then use it or create a it
    obj, created = Order.objects.get_or_create(
        user=request.user,
        status=OrderStatus.objects.get(pk=1)
        )

    try:
        pizza_name_id = int(request.POST["pizza_name"])
        pizza_size_id = int(request.POST["pizza_size"])
        pizza_topping_combo_id = int(request.POST["pizza_topping_combo"])
        pizza_count = int(request.POST["count"])
        
    # find pizza in BD
        pizza = Pizza.objects.get(name=pizza_name_id, size=pizza_size_id, combo=pizza_topping_combo_id)
    
    # todo: this exception needs tuning 
    except Pizza.DoesNotExist:
        return render(request, "orders/error.html", {"message": "That Pizza Does not Exist."})
    
    # create a new order item and save it to DB
    pizza_order = PizzaOrderItem(pizza=pizza, count=pizza_count, order=obj)
    pizza_order.save()

    # calculate total price
    total_price = 0
    pizzas = obj.pizzas.all()
    for p in pizzas:
        order_item_price = p.pizza.price * p.count
        total_price += order_item_price

    # save total price to current order
    obj.price = total_price
    obj.save()

    # get all toppings
    pizza_toppings = request.POST.getlist("pizza_toppings")
    
    if pizza_toppings is not None:
        for topping in pizza_toppings:
            pizza_order.toppings.add(topping)

    return HttpResponseRedirect(reverse("index"))

def cart_sub_view(request):
    # add check if cart is already in created, then use it or create a it
    obj, created = Order.objects.get_or_create(
        user=request.user,
        status=OrderStatus.objects.get(pk=1)
        )

    try:
        sub_name_id = int(request.POST["sub_name"])
        sub_size_id = int(request.POST["sub_size"])
        sub_count = int(request.POST["count"])

        sub = Sub.objects.get(name=sub_name_id, size=sub_size_id)
    except Sub.DoesNotExist:
        return render(request, "orders/error.html", {"message": "That Sub Does not Exist."})
    
    sub_order = SubOrderItem(sub=sub, count=sub_count, order=obj)
    sub_order.save()

    # get all add-ons
    sub_add_ons = request.POST.getlist("sub_add_ons")
    print ("\n", sub_add_ons, "\n")
    
    if sub_add_ons is not None:
        for add_on in sub_add_ons:
            sub_order.add_ons.add(add_on)

    return HttpResponseRedirect(reverse("index"))
    
def cart_dinner_platter_view(request):
    # add check if cart is already in created, then use it or create a it
    obj, created = Order.objects.get_or_create(
        user=request.user,
        status=OrderStatus.objects.get(pk=1)
        )

    dinner_platter_name_id = int(request.POST["dinner_platter_name"])
    dinner_platter_size_id = int(request.POST["dinner_platter_size"])
    dinner_platter_count = int(request.POST["count"])

    dinner_platter = DinnerPlatter.objects.get(name=dinner_platter_name_id, size=dinner_platter_size_id)
    dinner_platter_order = DinnerPlatterOrderItem(dinner_platter=dinner_platter, count=dinner_platter_count, order=obj)
    dinner_platter_order.save()

    return HttpResponseRedirect(reverse("index"))

def cart_pasta_view(request):
    # add check if cart is already in created, then use it or create a it
    obj, created = Order.objects.get_or_create(
        user=request.user,
        status=OrderStatus.objects.get(pk=1)
        )

    pasta_id = int(request.POST["pasta_name_price"])
    pasta_count = int(request.POST["count"])

    pasta = Pasta.objects.get(id=pasta_id)
    pasta_order = PastaOrderItem(pasta=pasta, count=pasta_count, order=obj)
    pasta_order.save()

    return HttpResponseRedirect(reverse("index"))

def cart_salad_view(request):
    # add check if cart is already in created, then use it or create a it
    obj, created = Order.objects.get_or_create(
        user=request.user,
        status=OrderStatus.objects.get(pk=1)
        )

    salad_id = int(request.POST["salad_name_price"])
    salad_count = int(request.POST["count"])

    salad = Salad.objects.get(id=salad_id)
    salad_order = SaladOrderItem(salad=salad, count=salad_count, order=obj)
    salad_order.save()

    return HttpResponseRedirect(reverse("index"))

#endregion Cart views

def order_view(request, order_id): # get order ID
    print ("\n","trying to put order #: " + str(order_id), "\n")
    
    # change the status of the order
    order = Order.objects.get(pk=order_id)
    
    second_order_status = OrderStatus.objects.get(pk=2)
    print ("second_order_status is:" + str(second_order_status))

    order.status = second_order_status

    # add address to the order
    address = request.POST["address"]
    order.address = address
    
    order.save()
    print ("new order_status is:" + str(order.status))
    print ("address is:" + order.address)

    return render(request, "orders/success.html", {"message": "Order accepted! Order number: " + str(order.id)})
