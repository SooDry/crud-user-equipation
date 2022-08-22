from django.contrib import messages
from django.shortcuts import render, redirect

from User.models import User


def register(request):
    if request.method == 'POST':
        identification = request.POST['identification']
        name = request.POST['name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(identification=identification).exists():
                messages.info(request, 'Identificacion ya se encuentra en uso')
                return redirect(register)
            else:
                user = User.objects.create(identification=identification, password=password,
                                           name=name, last_name=last_name)
                user.save()

                return redirect('/')
        else:
            messages.info(request, 'Las contraseñas no son iguales')
            return redirect(register)
    else:
        return render(request, 'registration.html')


def login_user(request):
    if request.method == 'POST':
        identification = request.POST['identification']
        password = request.POST['password']

        try:
            user = User.objects.get(identification=identification, password=password)
            return redirect('/users')
        except:
            messages.info(request, 'Usuario o contraseña invalido')
            return redirect('/')
    else:
        return render(request, 'login.html')
