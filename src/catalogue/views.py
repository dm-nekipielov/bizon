from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from catalogue.models import Category, SubCategory, Product
from catalogue.tasks import (generate_categories, generate_products,
                             generate_subcategories)


class IndexView(ListView):
    model = Category
    template_name = "index.html"


class SubcategoryView(DetailView):
    model = SubCategory
    template_name = "catalogue/subcategory.html"


class ProductView(DetailView):
    model = Product
    template_name = "catalogue/product-details.html"


def categories(request):
    generate_categories.delay()
    return HttpResponse("Generating categories")


def subcategories(request):
    generate_subcategories.delay()
    return HttpResponse("Generating subcategories")


def products(request):
    generate_products.delay()
    return HttpResponse("Generating categories")
