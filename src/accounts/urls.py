from django.urls import path

from accounts.views import Login, Registration, ActivateUser, ProfileView

app_name = "accounts"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("registration/", Registration.as_view(), name="registration"),
    path("activate/<str:uuid64>/<str:token>", ActivateUser.as_view(), name="activate_user"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
]