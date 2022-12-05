from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms_login import CreateUserForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers

# Create your views here.

def loginCheck(request):
    if request.user.is_authenticated :
        return render(request, 'formpage.html', {})
    else:
        form = UserCreationForm()

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Username atau Password salah")

        context = {'form': form}
        return render(request, 'login.html', context)

def loginPage(request):
    if request.user.is_authenticated :
        return redirect('/')
    else :
        form = UserCreationForm()

        if request.method == 'POST' :
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None :
                login(request, user)
                return redirect('/')
            else :
                messages.info(request, "Username atau Password salah")

        context = {'form' : form}
        return render(request, 'login.html', context)

def logoutUser(request) :
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def json_data(request) :
    if not request.user.is_staff :
        return redirect('/')
    else :
        data = serializers.serialize('json', User.objects.all())
        return HttpResponse(data, content_type="application/json")


@login_required(login_url="login")
def logoutUser(request) :
    logout(request)
    return redirect('/')

def registerPage(request) :
    form = CreateUserForm()

    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Pendaftaran akun " +user+" berhasil!" )



            return redirect('login')

    context = {'form' : form}
    return render(request, 'register.html', context)



