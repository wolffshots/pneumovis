from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages, auth
from django.contrib.auth.models import User

from .dash_apps import *

from .files import *

from django.conf import settings
from django.core.files.storage import FileSystemStorage


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
    if request.method == 'POST':

        if request.user.is_authenticated:
            user_id = request.user.id
            uploaded_file = request.FILES['file_upload']

            fs = FileSystemStorage()
            # TODO rename using date convention
            filename = fs.save(uploaded_file.name, uploaded_file)
            uploaded_file_url = fs.url(filename)
            delimiter = request.POST['delimiter']
            result = process_csv(uploaded_file_url, delimiter)
            messages.info(request, 'Successfully made ' +
                          str(result['s'])+' new entries and failed to make '+str(result['f'])+' entries')
            context = {'uploaded_file_url': uploaded_file_url}
            return render(request, 'pages/upload.html', context)
        else:
            messages.error(request, 'You have to be logged in to add swabs')
        return redirect('upload')

    else:
        return render(request, 'pages/upload.html')


def contact(request):
    # TODO add the Dr and our details
    return render(request, 'pages/contact.html')
