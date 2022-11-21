from django.urls import path

from cart.views import cart_summary, cart_add


app_name = "cart"
urlpatterns = [
    path("", cart_summary, name="cart_summary"),
    path("add/", cart_add, name="cart_add"),
]
