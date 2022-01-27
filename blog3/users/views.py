from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .form import LoginForm
from django.contrib.auth import authenticate, login, logout


def login_views(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)
        login(request,user)
        messages.success(request,"Başarıyla giriş yapıldı")
        return redirect('index')
    context = {
        'form':form
    }
    return render(request,'users/login.html',context)

def register_views(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Başarıyla kayıt yapıldı, giriş yapabilirsiniz")
        return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'users/register.html',context)

@login_required(login_url='/')
def logout_views(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı.",extra_tags="danger")
    return redirect('index')



