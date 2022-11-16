from _ast import Sub

from django.contrib import admin

from catalogue.models import Category, Order, Product, Subcategory

admin.site.register(
    [
        Category,
        Subcategory,
        Product,
    ]
)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total")
