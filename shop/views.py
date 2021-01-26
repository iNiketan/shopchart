from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Items


def frontpage(request):
    content = Items.objects.all()
    return render(request, 'shop/frontpage.html', {'content': content})

def addproduct(request):
    messages.success(request, 'Add Product')
    if request.method == 'POST':
        name = request.POST['name']
        sprice = request.POST['sprice']
        cprice = request.POST['cprice']
        imgs = request.FILES['imgs']
        data = Items(name=name, sprice=sprice, cprice=cprice, img=imgs)
        data.save()

    return render(request, 'shop/addproduct.html')

