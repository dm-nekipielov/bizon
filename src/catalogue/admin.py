from _ast import Sub

from django.contrib import admin

from catalogue.models import Category, SubCategory, Product, Order

admin.site.register([Category, SubCategory, Product, ])


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total")
