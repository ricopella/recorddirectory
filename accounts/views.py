from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserLoginForm

def login_view(request):
    """ admin task for authenticating login credentials """

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(form.cleaned_data)
    else:
        form = UserLoginForm(username, password)
    return render(request, "forms.html", {})

def base_view(request):
    """ testing home page """
    print("why are you sending here?") # Test 
    return render(request, "base.html",)


############# Original ###################
# def login_view(request):
#     """ admin task for authenticating login credentials """
#      form = UserLoginForm()  
#      if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect("base.html")
#     else:
#         form = UserLoginForm()
#     return render(request, "forms.html", {"form":form})
