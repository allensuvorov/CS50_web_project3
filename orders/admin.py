from django.contrib import admin

from .models import Pizza, PizzaName, PizzaSize, PizzaTopping, PizzaToppingCombo, Sub, SubName, SubSize, SubAddOn, Pasta, Salad, DinnerPlatter, DinnerPlatterName, DinnerPlatterSize, Order, OrderStatus, PizzaOrderItem, SubOrderItem, PastaOrderItem, SaladOrderItem, DinnerPlatterOrderItem

class PizzaOrderItemInLine(admin.TabularInline):
    model = PizzaOrderItem
    extra = 0

class SubOrderItemInLine(admin.TabularInline):
    model = SubOrderItem
    extra = 0

class PastaOrderItemInline(admin.TabularInline):
    model = PastaOrderItem
    extra = 0

class SaladOrderItemInline(admin.TabularInline):
    model = SaladOrderItem
    extra = 0

class DinnerPlatterOrderItemInline(admin.TabularInline):
    model = DinnerPlatterOrderItem
    extra = 0

class OrderAdmin (admin.ModelAdmin):
    inlines = [PizzaOrderItemInLine, SubOrderItemInLine, PastaOrderItemInline, SaladOrderItemInline, DinnerPlatterOrderItemInline]

# Register your models here.
admin.site.register(Pizza)
admin.site.register(PizzaName)
admin.site.register(PizzaSize)
admin.site.register(PizzaToppingCombo)
admin.site.register(PizzaTopping)
admin.site.register(Sub)
admin.site.register(SubName)
admin.site.register(SubSize)
admin.site.register(SubAddOn)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(DinnerPlatterName)
admin.site.register(DinnerPlatterSize)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus)
admin.site.register(PizzaOrderItem)
admin.site.register(SubOrderItem)
admin.site.register(PastaOrderItem)
admin.site.register(SaladOrderItem)
admin.site.register(DinnerPlatterOrderItem)
