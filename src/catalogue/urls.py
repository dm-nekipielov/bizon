from django.urls import path

from catalogue.views import (ProductListView, ProductView, SearchResultsView,
                             SubcategoryListView, generate_categories_view,
                             generate_products_view,
                             generate_subcategories_view)

app_name = "catalogue"
urlpatterns = [
    path("generate_categories/", generate_categories_view, name="generate_categories"),
    path("generate_subcategories/", generate_subcategories_view, name="generate_subcategories"),
    path("generate_products/", generate_products_view, name="generate_products"),
    path("category/<slug:slug>", SubcategoryListView.as_view(), name="category"),
    path("subcategory/<slug:slug>", ProductListView.as_view(), name="subcategory"),
    path("product/<slug:slug>", ProductView.as_view(), name="product"),
    path("search/", SearchResultsView.as_view(), name="search"),
]
