from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Subscription

@receiver(post_save, sender=get_user_model)
def create_subscription(sender, instance, created, **kwargs):
    print("Signal fired !!")
    if created:
        print("Element Created!")
        Subscription.objects.create(user=instance)