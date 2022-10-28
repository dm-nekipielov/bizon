from unittest.mock import ANY

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED,
                                   HTTP_404_NOT_FOUND)
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

    def test_product_details(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("api:product_detail", kwargs={"pk": self.product.pk}))
        self.assertEqual(response.status_code, HTTP_200_OK)

        self.assertEqual(
            response.data,
            {
                "id": 5,
                "name": "test_product",
                "price": "999.00",
                "code": 12345,
                "description": "Some test description",
                "stock": 1,
                "subcategory": 3,
            },
        )

    def test_product_create(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse("api:product_create"),
            data={
                "name": "test_product_2",
                "price": "1.00",
                "code": 12345,
                "description": "Some test description",
                "stock": 1,
                "subcategory": self.subcategory.pk,
            },
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_product_update_partly(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            reverse("api:product_update", kwargs={"pk": self.product.pk}), data={"name": "new product name"}
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": self.product.pk,
                "name": "new product name",
                "price": "999.00",
                "code": 12345,
                "description": "Some test description",
                "stock": 1,
                "subcategory": self.subcategory.pk,
            },
        )

    def test_product_update_fully(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            reverse("api:product_update", kwargs={"pk": self.product.pk}),
            data={
                "id": self.product.pk,
                "name": "Updated product name",
                "price": "1.00",
                "code": 11111,
                "description": "Updated description",
                "stock": 1,
                "subcategory": self.subcategory.pk,
            },
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": self.product.pk,
                "name": "Updated product name",
                "price": "1.00",
                "code": 11111,
                "description": "Updated description",
                "stock": 1,
                "subcategory": self.subcategory.pk,
            },
        )

    def test_product_details_not_authorised(self):
        response = self.client.get(reverse("api:product_detail", kwargs={"pk": self.product.pk}))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_product_not_exist(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("api:product_detail", kwargs={"pk": 10}))
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_product_delete(self):
        self.client.force_authenticate(user=self.user)
        self.product_2 = samples.sample_product(subcategory=self.subcategory, name="test_product_2", price=1)
        response = self.client.delete(reverse("api:product_delete", kwargs={"pk": self.product_2.pk}))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
