from django import forms
# from django.forms import ModelForm

class UserLoginForm(forms.Form):
    """ Login in form """
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
