from django.urls import path

from catalogue.views import generate_categories_view, generate_products_view, generate_subcategories_view, \
    ProductListView, ProductView, SubcategoryListView

app_name = "catalogue"
urlpatterns = [
    path("generate_categories/", generate_categories_view, name="generate_categories"),
    path("generate_subcategories/", generate_subcategories_view, name="generate_subcategories"),
    path("generate_products/", generate_products_view, name="generate_products"),
    path("category/<int:pk>", SubcategoryListView.as_view(), name="category"),
    path("subcategory/<int:pk>", ProductListView.as_view(), name="subcategory"),
    path("product/<int:pk>", ProductView.as_view(), name="product"),
]
