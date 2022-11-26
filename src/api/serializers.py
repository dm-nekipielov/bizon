from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from accounts.models import CustomUser
from catalogue.models import Category, Product, Subcategory


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "is_staff")


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "code", "in_stock", "subcategory")


class SubCategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = ("id", "name", "products", "category")


class CategorySerializer(ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "sub_categories")
