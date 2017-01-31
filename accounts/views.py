from django.contrib import messages
from django.shortcuts import render
from .forms import UserLoginForm
from .models import Accounts


def login_view(request):
    """ admin task for authenticating login credentials """
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

def base_view(request):
    """ testing home page """
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
