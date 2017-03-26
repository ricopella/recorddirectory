from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserLoginForm, UserSignupForm, ContactForm
from .models import Accounts, Catalog, Contact
from . import views


def login_view(request):
    """ login """
    form = UserLoginForm()
    if request.method == "POST":
        is_user = True
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

            try:
                user = Accounts.objects.get(username=username)
            except ObjectDoesNotExist: 
                is_user = False       
            if 'signup' in request.POST and is_user == False:
                user = Accounts()
                user.username = form.cleaned_data["username"]
                user.password = form.cleaned_data["password"]
                print(form.cleaned_data)
            elif 'login' in request.POST:
                if is_user == True:
                    if user.password == form.cleaned_data['password']:
                        return render(request, 'dashboard.html', {}) 
                    else:
                        messages.success(request, "invalid username & password")
                elif is_user == False:
                    return render(request, 'invalid.html', {})
            else:

                form = UserLoginForm()
                return render(request, 'dashboard.html', {})
    return render(request, "login.html", {"form": form})

def signup_view(request):
    """ Sign-Up View"""
    form = UserSignupForm()
    if request.method == "POST":
        is_user = True
        form = UserSignupForm(request.POST)
        if form.is_valid():
            if 'signup' in request.POST:
                
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
                print(form.cleaned_data)
                return render(request, 'dashboard.html')
        else:
            form = UserLoginForm()
            return render(request, 'dashboard.html', {} )
    return render(request, 'signup.html', {'form': form})


def contact_view(request):
    """ Contact Page View """
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            if 'submit' in request.POST:
                contact_ticket = Contact()
                contact_ticket.name = form.cleaned_data["name"]
                contact_ticket.number = form.cleaned_data["number"]
                contact_ticket.email = form.cleaned_data["email"]
                contact_ticket.description = form.cleaned_data["description"]
                contact_ticket.save()
                print(form.cleaned_data)
                return render(request, "dashboard.html")
        else:
            form = ContactForm()
            return render(request, 'dashboard.html', {})
    return render(request, "contact.html", {'form': form})

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
    """ Store/Dashboard View to display all products in database """
    if request.method =="GET":
        products = Catalog.objects.all()
        print (products)

        html_data = {}
        data = []
        for product in products:
            product_dict = {}
            product_dict["artist"] = product.artist
            product_dict["title"] = product.title
            product_dict["price"] = product.price
            product_dict["image"] = product.image
            data.append(product_dict)
<<<<<<< HEAD
    return render(request, "dashboard.html", {'data': data})
=======
        chunked_data = chunk_list(data, 3) # [[1,2,3], [4,5,6]]
    return render(request, "dashboard.html", {'data': chunked_data})


def chunk_list(data, chunkSize):
    """ loops through the data list from 'dashboard_view'
        to incriment through the products for readability
        on dashboard template """
    chunked_arr = []
    i = 0
    while (i < len(data)):
        chunked_arr.append(data[i:i + chunkSize])
        i += chunkSize
    print("chunked_arr:", chunked_arr) # Test for subarrays working properly
    return chunked_arr

            
>>>>>>> layout2
