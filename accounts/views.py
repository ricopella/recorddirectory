from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm
from .models import Accounts
from . import views


def signup_view(request):
    """ login """
    form = UserLoginForm()
    if request.method == "POST":
        is_user = True
        form = UserLoginForm(request.POST)
        if not form:
            messages.error(request, "Invalid login credentials")
        else:
            return render(request, "base.html", {})

        """ sign-up """
        if 'signup' in request.POST:
            if form.is_valid():
                user = Accounts()
                user.username = form.cleaned_data["username"]
                user.password = form.cleaned_data["password"]
                user.save()
                messages.success(request, 'Username & Password Created!')
            print(form.cleaned_data)
        elif 'signup' in request.POST:
            if is_user == True:
                if user.password == form.cleaned_data['password']:
                    return render(request, 'base.html', {})
                else:
                    messages.success(request, "invalid username & password")
            elif is_user == False:
                return render(request, 'invalid.html', {})
        else:
            form = UserLoginForm()
    return render(request, "forms.html", {"form": form})

def base_view(request):
    """ Home Page View """
    return render(request, "base.html",)

def invalid_view(request):
    """ Invalid Login View """
    return render(request, "invalid.html",)
