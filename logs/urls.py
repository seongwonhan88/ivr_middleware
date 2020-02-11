from django.urls import path
from .views import handle_payment
urlpatterns = [
    path('payment/', handle_payment)
]