from django.db import models
from django.contrib.auth import get_user_model

class Subscription(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)
    free_trial = models.BooleanField(default=True)
    card_token = models.TextField(default=str())
    card_add_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} Subscription"