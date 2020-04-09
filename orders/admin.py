from django.contrib import admin

from .models import Pizza, Pizza_name

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Pizza_name)