from django.urls import path
from catalogue.views import bitcoin, normalize_email

app_name = 'catalogue'
urlpatterns = [
    path("bitcoin/", bitcoin, name="bitcoin"),
    path("normalize_email/", normalize_email, name="normalize_email"),
]
