from django.urls import path, include
from checkout.views import payu_checkout, payu_success, payu_failure, HomeView, PayuView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Payu URLS
    path('payu', PayuView.as_view(), name='payu'),
    # path('payusuccess', PayuView.as_view(), name='payusuccess'),
    # path('payufailure', PayuView.as_view(), name='payufailure'),
    path('payu_checkout', payu_checkout, name="payu_checkout"),
    path('payu/failure', payu_failure, name="payufailure"),
    path('payu/success', payu_success, name="payusuccess"),
]