from django.http import HttpResponse
# temporary such that we can server hello world
from django.shortcuts import render, redirect
    
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from listings.choices import price_choices, bedroom_choices, state_choices

# from listings.models import listing as Listing
# from realtors.models import Realtor

# Create your views here.
import dash
import dash_core_components as dcc
import dash_html_components as html

from django_plotly_dash import DjangoDash

app = DjangoDash('SimpleExample')

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()}
                 for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i, 'value': j}
                 for i, j in [('L', 'large'), ('M', 'medium'), ('S', 'small')]],
        value='medium'
    ),
    html.Div(id='output-size')

])


@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value


@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." % (dropdown_size,
                                                   dropdown_color)

def index(request):
    # listings = Listing.objects.order_by(
    #     '-list_date').filter(published=True)[:3]

    # context = {
    #     'listings': listings,
    #     'state_choices': state_choices,
    #     'bedroom_choices': bedroom_choices,
    #     'price_choices': price_choices
    # }

    #return HttpResponse('<h1>Hello world</h1>')# we want to actually render a template but html can go here
    # takes in the request and the location of the template
    # return render(request, 'pages/index.html', context)
    # messages.error(request, 'Test?')
    return render(request, 'pages/index.html')


def about(request):
    # realtors = Realtor.objects.order_by('-hire_date')
    # mvps = Realtor.objects.all().filter(mvp=True)

    # context = {
    #     'realtors': realtors,
    #     'mvps': mvps
    # }
    # return render(request, 'pages/about.html', context)
    return render(request, 'pages/about.html')


# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         messages.success(request, 'Successfully logged out')
#         return redirect('index')

# def login(request):
#     # if request.method == 'POST':
#         # auth.logout(request)
#         # messages.success(request, 'Successfully logged out')
#     return render(request, 'pages/login.html')

def dashboard(request):
    return redirect('dashboard')

def dep(request):
    messages.error(request, 'Not yet implemented')
    return redirect('index')


# def register(request):
#     if request.method == 'POST':
#         # form submiusion
#         # print("submitted reg")
#         # messages.error(request, 'testing error message')
#         # return redirect('register')
#         # register logic

#         # Capture values
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

#         # check passwords
#         if password == password2:
#             # Check username
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'Username is already taken')
#                 return redirect('register')
#             else:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request, 'Email is already in use')
#                     return redirect('register')
#                 else:
#                     # Looks good
#                     # return redirect('register')
#                     # pass
#                     user = User.objects.create_user(
#                         username=username, password=password, email=email, first_name=first_name, last_name=last_name)
#                     # passwords are automagically hashed
#                     # Login after register

#                     ## Method 1 is to log straight in
#                     # auth.login(request,user)
#                     # messages.success(request,'You are now logged in')
#                     # return redirect('register')

#                     ## Method 2 is to save and redirect to log in
#                     user.save()
#                     messages.success(
#                         request, 'You are now registered, please log in')
#                     return redirect('login')
#         else:
#             messages.error(request, 'Passwords do not match')
#             return redirect('register')
#         pass
#     else:
#         return render(request, 'accounts/register.html')
#         return redirect('register')


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
