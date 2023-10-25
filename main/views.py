from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *

def index_view(request):

    return render(request, 'index.html')


def shop_view(request):
    return render(request, 'shop.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


def my_profile_view(request):
    return render(request, 'myprofile.html')



def signin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request,usr)
            return redirect('index_url')
    return render(request, 'log-in.html')


def signup_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('index_url')
    context = {

    }
    return render(request,'sign_up.html')


