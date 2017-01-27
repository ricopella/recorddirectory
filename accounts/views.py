from django.contrib.auth import(
authenticate,
get_user_model,
login,
logout,
)

from django.shortcuts import render
from .forms import UserLoginForm

# Create your views here.

def login_view(request):
    """ login page """
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

    return render(request, "forms.html", {"form":form, "title": title})

# def login_create_new_view(request): # view for new user
#     return render(request, "form.html", {})

# def login_retrieve_new_view(request): # view for existing user & checks password
#     return render(request, "form.html", {})

# def login_success_view(request): # view for successful login
#     return render(request, "form.html", {})

# def login_fail_view(request): # view for failure login
#     return render(request, "form.html", {})