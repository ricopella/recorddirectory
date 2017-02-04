from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^', views.signup_view, name='Login'),
    url(r'^invalid', views.signup_view, name='Invalid')
]
