from . import views
from django.conf.urls import url
import django.contrib.auth.views

urlpatterns = [
    url(r'^login/$', views.signin, name='login'),
    url(r'^signout/$', views.signout, name='signout'),

    # login / logout urls
    # url(r'^login/$',
    #     django.contrib.auth.views.LoginView,
    #     name='login'),
    # url(r'^logout/$',
    #     django.contrib.auth.views.LogoutView,
    #     name='logout'),
    # url(r'^logout-then-login/$', 
    #     django.contrib.auth.views.logout_then_login, 
    #     name='logout_then_login'),
]