from django.shortcuts import render, redirect, HttpResponse

from django.http import HttpResponseRedirect

# Create your views here.
def base_view(request):
    return render(request, "base.html",)
