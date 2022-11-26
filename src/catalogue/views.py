from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from catalogue.models import Category, Product, Subcategory
from catalogue.tasks import (generate_categories, generate_products,
                             generate_subcategories)


class IndexView(ListView):
    model = Category
    template_name = "index.html"
    context_object_name = "categories"


class SearchResultsView(ListView):
    model = Product
    template_name = "catalogue/search.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Product.objects.filter(name__icontains=query)


class SubcategoryListView(ListView):
    model = Subcategory
    template_name = "catalogue/subcategory_list.html"
    context_object_name = "subcategories"
    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return Subcategory.objects.filter(
            category=category,
        )


class ProductListView(ListView):
    model = Product
    template_name = "catalogue/product_list.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        subcategory = get_object_or_404(Subcategory, slug=self.kwargs["slug"])
        return Product.objects.filter(
            subcategory=subcategory,
        )


class ProductView(DetailView):
    model = Product
    template_name = "catalogue/product_details.html"


def generate_categories_view(request):
    generate_categories.delay()
    return HttpResponse("Generating categories")


def generate_subcategories_view(request):
    generate_subcategories.delay()
    return HttpResponse("Generating subcategories")


def generate_products_view(request):
    generate_products.delay()
    return HttpResponse("Generating categories")
