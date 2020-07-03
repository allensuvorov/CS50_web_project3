from django.contrib import admin

from .models import Pizza, Pizza_name, Pizza_size, Pizza_topping, Pizza_topping_combo, Sub, Sub_name, Sub_size, Sub_add_on, Pasta, Salad, Dinner_platter, Order, Order_status, Pizza_order_item

class PizzaOrderItemInLine(admin.TabularInline):
    model = Pizza_order_item
    extra = 1

class OrderAdmin (admin.ModelAdmin):
    inlines = [PizzaOrderItemInLine]

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Pizza_name)
admin.site.register(Pizza_size)
admin.site.register(Pizza_topping_combo)
admin.site.register(Pizza_topping)
admin.site.register(Sub)
admin.site.register(Sub_name)
admin.site.register(Sub_size)
admin.site.register(Sub_add_on)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_platter)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_status)
admin.site.register(Pizza_order_item)