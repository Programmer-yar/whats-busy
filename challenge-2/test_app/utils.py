import datetime
from django.conf import settings
from test_app.models import Subscription
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def enable_subscription():
    unsubcribed = Subscription.objects.exclude(subscribed=True,
                                               subscription_cancelled=False)
    seven_days_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    trial_expired = unsubcribed.filter(card_add_date__lt=seven_days_ago)
    for sub in trial_expired:
        response = stripe.Subscription.create(
            customer=sub.stripe_customer_id,
            default_payment_method=sub.payment_method_id,
            # create a price object in stripe dashboard or using API
            items=[{"price": "price_1L29elA4nuJHTAQPp29pQDwJ"}],
            )
        sub.stripe_subscription_id = response["id"]
        sub.subscribed = True
        sub.free_trial = False
        sub.save()

