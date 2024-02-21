from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import PaymentListApiView


app_name = PaymentsConfig.name

urlpatterns = [
    path('payment/', PaymentListApiView.as_view(), name='payment_list'),
]