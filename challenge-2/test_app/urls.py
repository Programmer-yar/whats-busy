from django.urls import path
from .views import HomeView, AddCardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-card/', AddCardView.as_view(), name='add-card'),
]