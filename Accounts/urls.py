from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register),
    path("", views.login_user),
]