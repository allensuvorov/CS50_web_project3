from django.contrib import admin

from .models import Pizza, PizzaName, PizzaSize, PizzaTopping, Pizza_topping_combo, Sub, Sub_name, Sub_size, Sub_add_on, Pasta, Salad, Dinner_platter, Dinner_platter_name, Dinner_platter_size, Order, Order_status, Pizza_order_item, Sub_order_item, Pasta_order_item, Salad_order_item, Dinner_platter_order_item

class PizzaOrderItemInLine(admin.TabularInline):
    model = Pizza_order_item
    extra = 0

class SubOrderItemInLine(admin.TabularInline):
    model = Sub_order_item
    extra = 0

class PastaOrderItemInline(admin.TabularInline):
    model = Pasta_order_item
    extra = 0

class SaladOrderItemInline(admin.TabularInline):
    model = Salad_order_item
    extra = 0

class DinnerPlatterOrderItemInline(admin.TabularInline):
    model = Dinner_platter_order_item
    extra = 0

class OrderAdmin (admin.ModelAdmin):
    inlines = [PizzaOrderItemInLine, SubOrderItemInLine, PastaOrderItemInline, SaladOrderItemInline, DinnerPlatterOrderItemInline]

# Register your models here.
admin.site.register(Pizza)
admin.site.register(PizzaName)
admin.site.register(PizzaSize)
admin.site.register(Pizza_topping_combo)
admin.site.register(PizzaTopping)
admin.site.register(Sub)
admin.site.register(Sub_name)
admin.site.register(Sub_size)
admin.site.register(Sub_add_on)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_platter)
admin.site.register(Dinner_platter_name)
admin.site.register(Dinner_platter_size)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_status)
admin.site.register(Pizza_order_item)
admin.site.register(Sub_order_item)
admin.site.register(Pasta_order_item)
admin.site.register(Salad_order_item)
admin.site.register(Dinner_platter_order_item)
