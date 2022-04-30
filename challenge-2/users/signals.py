from django.db.models.signals import post_save
from django.dispatch import receiver
from test_app.models import Subscription
from .models import User

@receiver(post_save, sender=User)
def create_subscription(sender, instance, created, **kwargs):
    if created:
        Subscription.objects.create(user=instance)