from django.urls import path
from .views import home, payu_checkout, payu_failure, payu_success,\
                            paytm_checkout, paytm_response, cashfree_checkout, cashfree_response_return


urlpatterns = [
    path('', home, name="home"),
    path('payu_checkout', payu_checkout, name="payu_checkout"),
    path('paytm_checkout', paytm_checkout, name="paytm_checkout"),
    path('payu/failure', payu_failure, name="payu_failure"),
    path('payu/success', payu_success, name="payu_success"),
    path('paytm/response', paytm_response, name="paytm_response"),
    path('cashfree_checkout', cashfree_checkout, name="cashfree_checkout"),
    path('cashfree/response', cashfree_response_return, name="cashfree_response_return"),


]
