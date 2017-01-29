from django.contrib.auth import(
authenticate,
get_user_model,
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
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            return HttpResponseRedirect("base.html")
    else:
        form = UserLoginForm()
    return render(request, "forms.html", {"form":form})
