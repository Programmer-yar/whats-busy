from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from .forms import UserForm
from .views import CustomRegistrationView
urlpatterns = [
    path('register/',
         CustomRegistrationView.as_view(
            form_class=UserForm,
            template_name='users/register.html'
            ),
         name='django-registration-register'
         ),
    path('', include('django_registration.backends.activation.urls')),
]