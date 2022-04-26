"""Deployment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.index, name="index"),
    path('insurance/', views.home,name="home"),
    path('result/', views.result,name="result"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/login2.html", authentication_form=LoginForm), name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('profile/', views.index, name='profile'),
    path('accept/', views.accept, name='accept'),
    path('reject/', views.reject, name='reject'),
    path('premium/', views.premium, name='premium'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]
