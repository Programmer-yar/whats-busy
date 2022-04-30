from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from .forms import UserRegisterForm

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

class RegistrationView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = '/'