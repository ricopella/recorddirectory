from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist # <- need to import the error since it's a custom Djano error
from .forms import UserLoginForm
from .models import Accounts
from . import views


def signup_view(request):
    """ login """
    form = UserLoginForm()
    if request.method == "POST":
        is_user = True
        form = UserLoginForm(request.POST)

        # need to validate the form before doing anyting else
        if form.is_valid():
            # grap the username from the form to test if 
            # user already exists
            username = form.cleaned_data['username']

            # if not form: <- this will always be false. We get the form no matter what
            #     messages.error(request, "Invalid login credentials")
            # else:
            #     return render(request, "base.html", {}) <- best practice to have base just before style/sturcture
                                                            # you might want to add a seperate index.html that extends base

            try: # <- we need to try to get the user expecting it might fail if they don't exist
                user = Accounts.objects.get(username=username)
            except ObjectDoesNotExist: # <- here is where we catch or 'except' the error so the app doesn't crash
                is_user = False        # found the specific error here http://stackoverflow.com/questions/11109468/how-do-i-import-the-django-doesnotexist-exception
            if 'signup' in request.POST and is_user == False: # <- need to check if they clicked signup and
                user = Accounts()                             # that they don't exist to prevent duplicate entries
                user.username = form.cleaned_data["username"] # this model logic should work now
                user.password = form.cleaned_data["password"]
                user.save()
                messages.success(request, 'Username & Password Created!')
                print(form.cleaned_data)
            elif 'login' in request.POST:
                if is_user == True:
                    if user.password == form.cleaned_data['password']:
                        return render(request, 'base.html', {}) # <- same thing as about about index.html
                    else:
                        messages.success(request, "invalid username & password")
                elif is_user == False:
                    return render(request, 'invalid.html', {})
            else:
                # Need to setup redirect to home page also
                form = UserLoginForm()       
    return render(request, "forms.html", {"form": form})

def base_view(request):
    """ Home Page View """
    return render(request, "base.html",)

def invalid_view(request):
    """ Invalid Login View """
    return render(request, "invalid.html",)
