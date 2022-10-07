from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient

from utils import samples


class TestAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = samples.sample_category(name="test_category")
        self.subcategory = samples.sample_subcategory(
            category=self.category,
            name="test_subcategory",
        )
        self.product = samples.sample_product(subcategory=self.subcategory, name="test_product", price=999)
        self.user = get_user_model().objects.create(email="test_user@email.com")
        self.user.set_password("qwerty")
        self.user.save()

    def test_product_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("api:product_detail", kwargs={"pk": self.product.pk}))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "name": "test_product",
                "price": "999.00",
                "code": 12345,
                "description": "Some test description",
                "stock": 1,
                "subcategory": 1,
            },
        )
