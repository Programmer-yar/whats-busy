from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    # def post(self, request):
    #     return redirect('home')

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'