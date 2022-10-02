from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from accounts.models import CustomUser
from catalogue.models import Product, SubCategory, Category


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'is_staff')


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')


class SubCategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'products')


class CategorySerializer(ModelSerializer):
    subcategory = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategory')
