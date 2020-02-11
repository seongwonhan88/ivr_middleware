import stripe

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ivr_payment import settings
from logs.serializers import CreditCardSerializer

from logs.handler import card_formatter


@api_view(['POST'])
def handle_payment(request):
    """
    1) Takes only POST request from IVR in JSON format
    2) Send request to Stripe once formatted
    3) Forward Stripe response
    """
    serializer = CreditCardSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        formatted_card = card_formatter(serializer.data)

        try:
            stripe.api_key = settings.stripe_key
            intent = stripe.PaymentMethod.create(type="card", card=formatted_card)
            return Response(intent)

        except stripe.error.InvalidRequestError as e:
            return_data = {"status": e.http_status, "error": e.error}
            return Response(return_data, status=e.http_status)
