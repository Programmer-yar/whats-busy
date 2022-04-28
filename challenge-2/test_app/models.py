from django.db import models
from django.contrib.auth import get_user_model

class Subscription(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True)
    free_trial = models.BooleanField(default=True)
    fee_charged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} Subscription"