import datetime

from django.shortcuts import render, redirect

from Equipments.models import Equipments
from .models import User
from cryptography.fernet import Fernet

# Create your views here.

key = Fernet.generate_key()
fernet = Fernet(key)


def home(request):
    list_user = User.objects.all()
    list_equipment = Equipments.objects.all()

    return render(request, "user.html", {"users": list_user, "equipment": list_equipment})


def new_user(request):
    identification = request.POST.get('identification', 0)
    name = request.POST.get('name', '')
    last_name = request.POST.get('last_name', '')
    equipment = request.POST.get('equipment', '')
    save_user = datetime.datetime.now()

    user = User.objects.create(identification=identification, name=name, last_name=last_name,
                               equipment=equipment, save_user=save_user)
    return redirect('/users')


def get_user(request, identification):
    user = User.objects.get(identification=identification)
    list_equipment = Equipments.objects.all()
    return render(request, "editUser.html", {"user": user, "equipment": list_equipment})


def edit_user(request):
    identification = request.POST.get('identification', 0)
    name = request.POST.get('name', '')
    last_name = request.POST.get('last_name', '')
    password = request.POST.get('password', '')
    encode_password = fernet.encrypt(password.encode())
    user = User.objects.get(identification=identification)
    equipment = request.POST.get('equipment', '')
    user.name = name
    user.last_name = last_name
    user.password = encode_password
    user.equipment = equipment
    user.save()
    return redirect('/users')


def delete_user(request, identification):
    user = User.objects.get(identification=identification)
    user.delete()
    return redirect('/users')
