from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class TestCustomUser(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email="user@email.com")
        self.user.set_password("qwerty")
        self.user.save()

        self.admin = get_user_model().objects.create(
            email="admin@email.com",
            is_staff=True,
        )
        self.admin.set_password("qwerty")
        self.admin.save()

        self.client = Client()

    def test_user_login_wrong_email(self):
        user_login = self.client.login(
            email="wrong_email",
            password="qwerty",
        )
        self.assertFalse(user_login)

    def test_user_login_wrong_password(self):
        user_login = self.client.login(
            email="user@email.com",
            password="wrong_password",
        )
        self.assertFalse(user_login)

    def test_user_access_admin_panel(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_admin_access_admin_panel(self):
        self.client.force_login(self.admin)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
