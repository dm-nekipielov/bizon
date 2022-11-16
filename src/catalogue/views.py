from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from catalogue.models import Category, Subcategory, Product
from catalogue.tasks import (generate_categories, generate_products,
                             generate_subcategories)


class IndexView(ListView):
    model = Category
    template_name = "index.html"


class SubcategoryListView(ListView):
    model = Subcategory
    template_name = "catalogue/subcategory_list.html"
    context_object_name = 'subcategories'
    paginate_by = 1

    def get_queryset(self):
        return Subcategory.objects.filter(
            category_id=self.kwargs['pk'],
        )


class ProductListView(ListView):
    model = Product
    template_name = "catalogue/product_list.html"
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        return Product.objects.filter(
            subcategory_id=self.kwargs['pk'],
        )


class ProductView(DetailView):
    model = Product
    template_name = "catalogue/product_details.html"


def categories(request):
    generate_categories.delay()
    return HttpResponse("Generating categories")


def subcategories(request):
    generate_subcategories.delay()
    return HttpResponse("Generating subcategories")


def products(request):
    generate_products.delay()
    return HttpResponse("Generating categories")
