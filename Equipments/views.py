from django.shortcuts import render, redirect
from .models import Equipments


# Create your views here.

def home(request):
    list_equipment = Equipments.objects.all()
    return render(request, "equipments.html", {"equipments": list_equipment})

def new_equipment(request):
    code = request.POST['code']
    brand = request.POST['brand']
    sku = request.POST['sku']

    equipment = Equipments.objects.create(code=code, brand=brand, sku=sku)
    return redirect('/equipments')


def get_equipment(request, code):
    equipment = Equipments.objects.get(code=code)
    return render(request, "editEquipment.html", {"equipment": equipment})


def edit_equipment(request):
    code = request.POST['code']
    brand = request.POST['brand']
    sku = request.POST['sku']
    equipment = Equipments.objects.get(code=code)
    equipment.brand = brand
    equipment.sku = sku
    equipment.save()

    return redirect('/equipments')


def delete_equipment(request, code):
    user = Equipments.objects.get(code=code)
    user.delete()
    return redirect('/equipments')
