from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserLoginForm, UserSignupForm
from .models import Accounts, Catalog, Artist, Label, Genre, Status
from . import views


def login_view(request):
    """ login """
    form = UserLoginForm()
    if request.method == "POST":
        is_user = True
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

            try: # <- we need to try to get the user expecting it might fail if they don't exist
                user = Accounts.objects.get(username=username)
            except ObjectDoesNotExist: # <- here is where we catch or 'except' the error so the app doesn't crash
                is_user = False        # found the specific error here http://stackoverflow.com/questions/11109468/how-do-i-import-the-django-doesnotexist-exception
            if 'signup' in request.POST and is_user == False:
                user = Accounts()
                user.username = form.cleaned_data["username"]
                user.password = form.cleaned_data["password"]
                user.save()
                messages.success(request, 'Username & Password Created!')
                print("It's sending to login form")
                print(form.cleaned_data)
            elif 'login' in request.POST:
                if is_user == True:
                    if user.password == form.cleaned_data['password']:
                        print ('success!') # test
                        return render(request, 'index.html', {}) # <- same thing as about index.html
                    else:
                        messages.success(request, "invalid username & password")
                elif is_user == False:
                    return render(request, 'invalid.html', {})
            else:

                form = UserLoginForm()
                return render(request, 'index.html', {}) # Need to setup redirect to home page also
    return render(request, "login.html", {"form": form})

def signup_view(request):
    """ Sign-Up View"""
    form = UserSignupForm()
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = Accounts()
            user.username = form.cleaned_data["username"]
            user.password = form.cleaned_data["password"]
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.street_address1 = form.cleaned_data["street_address1"]
            user.street_address2 = form.cleaned_data["street_address2"]
            user.city = form.cleaned_data["city"]
            user.state = form.cleaned_data["state"]
            user.country = form.cleaned_data["country"]
            user.phone = form.cleaned_data["phone"]
            user.email = form.cleaned_data["email"]
            user.save()
            messages.success(request, 'Username & Password Created!')
            print(form.cleaned_data)
        else:
            form = UserLoginForm()
            return render(request, 'dashboard.html', {} )
    return render(request, 'signup.html', {'form': form})


def base_view(request):
    """ Home Page View """
    return render(request, "base.html",)

def invalid_view(request):
    """ Invalid Login View """
    return render(request, "invalid.html",)

def index_view(request):
    """ Invalid Login View """
    return render(request, "index.html",)

def dashboard_view(request):
    """ Store/Dashboard View """
    products = Catalog()
    if request.method =="GET":
        products = Catalog(request.GET)
        print (products)
    
    return render(request, "dashboard.html", products)
