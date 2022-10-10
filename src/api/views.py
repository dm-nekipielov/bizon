from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from accounts.models import CustomUser
from api.serializers import (CategorySerializer, CustomUserSerializer,
                             ProductSerializer, SubCategorySerializer)
from catalogue.models import Category, Product, SubCategory


class ProductMixin:
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SubCategoryMixin:
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CategoryMixin:
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ProductDetailView(ProductMixin, RetrieveAPIView):
    pass


class ProductListView(ProductMixin, ListAPIView):
    pass


class ProductCreateView(ProductMixin, CreateAPIView):
    pass


class ProductUpdateView(ProductMixin, UpdateAPIView):
    pass


class ProductDeleteView(ProductMixin, DestroyAPIView):
    pass


class SubCategoryListView(SubCategoryMixin, ListAPIView):
    pass


class SubCategoryDetailView(SubCategoryMixin, RetrieveAPIView):
    pass


class SubCategoryCreateView(SubCategoryMixin, CreateAPIView):
    pass


class SubCategoryUpdateView(SubCategoryMixin, UpdateAPIView):
    pass


class SubCategoryDeleteView(SubCategoryMixin, DestroyAPIView):
    pass


class CategoryListView(CategoryMixin, ListAPIView):
    pass


class CategoryDetailView(CategoryMixin, RetrieveAPIView):
    pass


class CategoryCreateView(CategoryMixin, CreateAPIView):
    pass


class CategoryUpdateView(CategoryMixin, UpdateAPIView):
    pass


class CategoryDeleteView(CategoryMixin, DestroyAPIView):
    pass
