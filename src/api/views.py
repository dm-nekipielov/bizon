from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from accounts.models import CustomUser
from api.serializers import CustomUserSerializer, ProductSerializer, \
    SubCategorySerializer, CategorySerializer
from catalogue.models import Product, SubCategory, Category


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SubCategoryListView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryDetailView(RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
