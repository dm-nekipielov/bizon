from django.urls import include, path
from rest_framework import routers

from api.views import (CategoryCreateView, CategoryDeleteView,
                       CategoryDetailView, CategoryListView,
                       CategoryUpdateView, ProductCreateView,
                       ProductDeleteView, ProductDetailView, ProductListView,
                       ProductUpdateView, SubCategoryCreateView,
                       SubCategoryDeleteView, SubCategoryDetailView,
                       SubCategoryListView, SubCategoryUpdateView, UserViewSet)

app_name = "api"
routes = routers.DefaultRouter()
routes.register("customers", UserViewSet)

urlpatterns = [
    path("", include(routes.urls)),
    path("auth/", include("rest_framework.urls")),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("category/create/", CategoryCreateView.as_view(), name="product_create"),
    path("category/<int:pk>/update/", CategoryUpdateView.as_view(), name="product_create"),
    path("category/<int:pk>/delete/", CategoryDeleteView.as_view(), name="product_create"),
    path("subcategory/", SubCategoryListView.as_view(), name="subcategory_list"),
    path("subcategory/<int:pk>/", SubCategoryDetailView.as_view(), name="subcategory_detail"),
    path("subcategory/create/", SubCategoryCreateView.as_view(), name="product_create"),
    path("subcategory/<int:pk>/update/", SubCategoryUpdateView.as_view(), name="product_create"),
    path("subcategory/<int:pk>/delete/", SubCategoryDeleteView.as_view(), name="product_create"),
    path("product/", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_create"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_create"),
]
