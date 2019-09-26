from django.urls import path
from .views import home, payu_checkout, payu_failure, payu_success,\
                            paytm_checkout, paytm_response, stripe_checkout


urlpatterns = [
    path('', home, name="home"),
    path('payu_checkout', payu_checkout, name="payu_checkout"),
    path('paytm_checkout', paytm_checkout, name="paytm_checkout"),
    path('payu/failure', payu_failure, name="payu_failure"),
    path('payu/success', payu_success, name="payu_success"),
    path('paytm/response', paytm_response, name="paytm_response"),
    path('stripe_checkout', stripe_checkout, name="stripe_checkout"),
]
