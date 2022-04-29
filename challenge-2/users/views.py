from django.shortcuts import render
from django_registration.views import RegistrationView

class CustomRegistrationView(RegistrationView):
    def register(self):
        print(self.request.POST)
        print(self.form)