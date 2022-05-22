import datetime
from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse
from django.conf import settings

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

class HomeView(LoginRequiredMixin, View):
    template_name = 'test_app/home.html'

    def get(self, request, *args, **kwargs):
        user_sub = request.user.subscription
        if not user_sub.card_valid:
            return redirect(reverse('add-card'))
        return render(request, self.template_name)

class AddCardView(LoginRequiredMixin, View):
    template_name = 'test_app/add_card.html'

    def get(self, request, *args, **kwargs):
        user_subscription = request.user.subscription
        if user_subscription.card_valid:
            return redirect(reverse('home'))
        customer_id = user_subscription.stripe_customer_id
        if not user_subscription.stripe_customer_id:
            customer = stripe.Customer.create()
            customer_id = customer['id']
            user_subscription.stripe_customer_id = customer_id
            user_subscription.save()

        intent = stripe.SetupIntent.create(customer=customer_id)

        context = { 'client_secret': intent.client_secret }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_subscription = request.user.subscription
        user_subscription.payment_method_id = request.POST.get('paymentMethod')
        stripe.PaymentMethod.attach(
            user_subscription.payment_method_id,
            customer=user_subscription.stripe_customer_id
            )
        user_subscription.card_valid = True
        user_subscription.card_add_date = datetime.datetime.now()
        user_subscription.save()
        return redirect(reverse('home'))


class CancelSubView(LoginRequiredMixin, View):
    template_name = 'test_app/cancel_sub.html'
    def get(self, request, *args, **kwargs):
        user_subscription = request.user.subscription
        stripe.Subscription.delete(user_subscription.stripe_subscription_id)
        user_subscription.subscription_cancelled = True
        user_subscription.save()
        return render(request, self.template_name)