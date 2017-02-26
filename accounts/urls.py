from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [ 
    url(r'^$', views.index_view, name="main"),
    url(r'^home/', views.index_view, name='home'),
    url(r'^login', views.login_view, name='login'),
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^invalid/', views.invalid_view, name='invalid'),
    url(r'^index/', views.index_view, name='index'),
    url(r'^store/', views.dashboard_view, name='store'),
]
