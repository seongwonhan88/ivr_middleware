from django.urls import path

from .views import view_payment

urlpatterns = [
    path('payment/', view_payment)
]
