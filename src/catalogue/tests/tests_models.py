from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from utils.samples import (sample_category, sample_order, sample_product,
                                sample_subcategory)


class TestProductModel(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email="some@test.mail", password="somepassword")
        self.test_category = sample_category(name="test_category")
        self.test_subcategory = sample_subcategory(name="test_subcategory", category=self.test_category)
        self.test_product = sample_product(name="test_product", subcategory=self.test_subcategory, price=999)
        self.test_product_2 = sample_product(name="test_product_2", subcategory=self.test_subcategory, price=1)
        self.test_order = sample_order(self.user, [self.test_product, self.test_product_2])

    def test_order_total(self):
        self.assertEqual(self.test_order.total(), 1000)

    def test_product_name_limit(self):
        with self.assertRaises(ValidationError):
            sample_product(name="*" * 201, subcategory=self.test_subcategory, price=2)

    def test_product_price_type(self):
        with self.assertRaises(ValidationError):
            sample_product(name="test_product_3", subcategory=self.test_subcategory, price="text")

    def test_product_price_decimal_places(self):
        with self.assertRaises(ValidationError):
            sample_product(name="test_product_3", subcategory=self.test_subcategory, price=1.033)
