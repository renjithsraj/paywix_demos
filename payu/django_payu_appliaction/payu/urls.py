from django.urls import path
from . import views

app_name = "appname"
urlpatterns = [
    path('payment', views.payment, name="payment"),
    path('payment/success', views.payment_success, name="payment_success"),
    path('payment/failure', views.payment_failure, name="payment_failure"),
]