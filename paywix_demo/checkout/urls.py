from django.urls import path
from checkout.views import home


urlpatterns = [
    path('', home, name="home")
]
