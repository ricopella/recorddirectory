from django.contrib.auth import(
authenticate,
login,
logout,
)

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserLoginForm

# Create your views here.

def login_view(request):
    """ admin task for authenticating login credentials """
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("base.html")
    else:
        form = UserLoginForm()
    return render(request, "forms.html", {"form":form})

def base_view(request):
    """ testing home page """
    print("why are you sending here?")
    return render(request, "base.html",)

# def login_view(request):
#     """ admin task for authenticating login credentials """
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect("base.html")
#     else:
#         form = UserLoginForm()
#     return render(request, "forms.html", {"form":form})
