from django import forms
from subscriptions.models import Subscription

class SubscriptionForm(forms.ModelForm):
    class meta:
        model = Subscription
        exclude = ('created_at',)