from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

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

schema_view = get_schema_view(
    openapi.Info(
        title="Bizon API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("", include(routes.urls)),
    path("auth/", include("rest_framework.urls")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    path("auth/", include("djoser.urls.jwt")),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    path("category/<int:pk>/update/", CategoryUpdateView.as_view(), name="category_update"),
    path("category/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),
    path("subcategory/", SubCategoryListView.as_view(), name="subcategory_list"),
    path("subcategory/<int:pk>/", SubCategoryDetailView.as_view(), name="subcategory_detail"),
    path("subcategory/create/", SubCategoryCreateView.as_view(), name="subcategory_create"),
    path("subcategory/<int:pk>/update/", SubCategoryUpdateView.as_view(), name="subcategory_update"),
    path("subcategory/<int:pk>/delete/", SubCategoryDeleteView.as_view(), name="subcategory_delete"),
    path("product/", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
