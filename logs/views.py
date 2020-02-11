import stripe

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ivr_payment import settings
from logs.serializers import CreditCardSerializer

from logs.handler import handle_card_format


@api_view(['POST'])
def view_payment(request):
    """
    1) Takes only POST request from IVR in JSON format
    2) Send request to Stripe once formatted
    3) Forward Stripe response
    """
    serializer = CreditCardSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): # IVR sent data's field validation is handled here
        formatted_card = handle_card_format(serializer.data)

        try: # attempt to make transaction to Stripe with api key and IVR given data
            stripe.api_key = settings.stripe_key
            response = stripe.PaymentMethod.create(type="card", card=formatted_card)
            return_data = {"transaction": "success", "object": response.object, "type": response.type}
            return Response(return_data) # if succeeded, default http status is 200

        except stripe.error.InvalidRequestError as e:
            return Response(data={"stripe_error": e.error}, status=e.http_status)
