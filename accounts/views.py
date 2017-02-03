from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm
from .models import Accounts
from . import views


def signup_view(request):
    """ task for creating new credentials """
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = Accounts()
            user.username = form.cleaned_data["username"]
            user.password = form.cleaned_data["password"]
            user.save()
            messages.success(request, 'Username & Password Created!')
            print(form.cleaned_data)
        else:
            form = UserLoginForm()
    return render(request, "forms.html", {"form": form})

def login_view(request):
    """ admin task for authenticating login credentials """
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("base.html")
    else:
        return ("Username & Password do not match")
    return render(request, "forms.html", {"form":form})

def base_view(request):
    """ Home Page View """
    return render(request, "base.html",)

