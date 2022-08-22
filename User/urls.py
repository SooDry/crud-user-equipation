from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newUser/', views.new_user),
    path('getUser/<identification>', views.get_user),
    path('editUser/', views.edit_user),
    path('deleteUser/<identification>', views.delete_user)
]
