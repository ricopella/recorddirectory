from django import forms

class UserLoginForm(forms.Form):
    """ Login in form """
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class UserSignupForm(forms.Form):
    """ sign-up in form """
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)
    street_address1 = forms.CharField(max_length=120)
    street_address2 = forms.CharField(max_length=120)
    city = forms.CharField(max_length=120)
    state = forms.CharField(max_length=3)
    country = forms.CharField(max_length=120)
    phone = forms.IntegerField()
    email = forms.EmailField(max_length=100)
