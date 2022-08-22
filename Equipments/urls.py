from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('newEquipment/', views.new_equipment),
    path('getEquipment/<code>', views.get_equipment),
    path('editEquipment/', views.edit_equipment),
    path('deleteEquipment/<code>', views.delete_equipment)
]
