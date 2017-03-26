from django import forms

class UserLoginForm(forms.Form):
    """ Login in form """
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class UserSignupForm(forms.Form):
    """ sign-up in form """
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(max_length=120, required=True)
    last_name = forms.CharField(max_length=120, required=True)
    street_address1 = forms.CharField(max_length=120, required=False)
    street_address2 = forms.CharField(max_length=120, required=False)
    city = forms.CharField(max_length=120, required=False)
    state = forms.CharField(max_length=3, required=False)
    country = forms.CharField(max_length=120, required=False)
    phone = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=100, required=False)

class ContactForm(forms.Form):
    """ Contact Us Form """
    name = forms.CharField(max_length=300)
    number = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=100, required=False)
    description = forms.CharField(widget=forms.Textarea)
