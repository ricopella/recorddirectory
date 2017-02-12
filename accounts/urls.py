from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [ # <- any urls specific to this app should go here. helps prevent duplicate urls
    #url(r'^', views.signup_view, name='Login'),
    url(r'^$', views.base_view, name="main"),
    url(r'^home/', views.base_view, name='home'),
    url(r'^login', views.login_view, name='login'),
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^invalid/', views.invalid_view, name='invalid'),
    url(r'^index/', views.index_view, name='index'),
    url(r'^store/', views.dashboard_view, name='store'),
]
