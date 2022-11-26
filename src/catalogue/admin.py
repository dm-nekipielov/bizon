from _ast import Sub

from django.contrib import admin

from catalogue.models import Category, Order, Product, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "category"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "in_stock", "is_active", "subcategory"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["is_active", "subcategory"]
    list_editable = ["price", "in_stock"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total")
