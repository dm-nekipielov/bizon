from django.urls import path

from catalogue.views import categories, products, subcategories, \
    ProductListView, ProductView, SubcategoryListView

app_name = "catalogue"
urlpatterns = [
    path("generate_categories/", categories, name="generate_categories"),
    path("generate_subcategories/", subcategories, name="generate_subcategories"),
    path("generate_products/", products, name="generate_products"),
    path("category/<int:pk>", SubcategoryListView.as_view(), name="category"),
    path("subcategory/<int:pk>", ProductListView.as_view(), name="subcategory"),
    path("product/<int:pk>", ProductView.as_view(), name="product"),
]
