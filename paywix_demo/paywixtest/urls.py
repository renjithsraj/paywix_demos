from django.urls import path
from .views import paywix_stripe_manage

urlpatterns = [
    path('paywix-stripe-checkout', paywix_stripe_manage, name="paywix_stripe")
]