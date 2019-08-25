from django.http import HttpResponse
# temporary such that we can server hello world
from django.shortcuts import render, redirect

from django.contrib import messages, auth
from django.contrib.auth.models import User
# this imports the app from a separate file (just for easier editing and modularity)
from .dash_app import *


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def dashboard(request):
    return redirect('dashboard')


def dep(request):
    messages.error(request, 'Not yet implemented')
    return redirect('index')


def login(request):
    if request.method == 'POST':
        # login logic
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'pages/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully logged out')
        return redirect('index')


def ip(request):
    return render(request, 'pages/index-proto.html')


def browse(request):
    return render(request, 'pages/browse.html')


def upload(request):
        # TODO check for authentication!
    return render(request, 'pages/upload.html')


def contact(request):
        # TODO add the Dr and our details
    return render(request, 'pages/contact.html')
