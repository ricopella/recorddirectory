from django import forms

class UserLoginForm(forms.Form):
    """ Login in form """
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
