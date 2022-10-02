from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet, ProductDetailView, SubCategoryDetailView, \
    CategoryDetailView, CategoryListView, SubCategoryListView

app_name = 'api'
routes = routers.DefaultRouter()
routes.register('customers', UserViewSet)

urlpatterns = [
    path("", include(routes.urls)),
    path("auth/", include("rest_framework.urls")),
    path("product/<int:pk>/", ProductDetailView.as_view(),
         name="product_detail"),
    path("subcategory/<int:pk>/", SubCategoryDetailView.as_view(),
         name="subcategory_detail"),
    path("subcategory/", SubCategoryListView.as_view(),
         name="subcategory_list"),
    path("category/<int:pk>/", CategoryDetailView.as_view(),
         name="category_detail"),
    path("category/", CategoryListView.as_view(),
         name="category_list"),
]
