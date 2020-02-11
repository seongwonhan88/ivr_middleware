import json

from logs.tasks import response_log_create, request_log_create


class CustomMiddleware(object):
    """Logs all REQUEST and RESPONSE made to/from the middleware application"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        request_log = self.log_request(request)
        response = self.get_response(request)

        self.log_response(response, request_log)

        # if the response contains detail error from stripe, the response is simplified
        self.simplify_stripe_response(response)
        return response

    @staticmethod
    def log_request(request):
        data = {"request_type": request.method, "url_path": request.get_full_path()}
        if request.body:  # only handle if the request body exists. Other field validations are handled at serializer
            request_body = json.loads(str(request.body, 'utf-8'))
            from logs.handler import handle_masking
            if "cc_num" in request_body:
                request_body["cc_num"] = handle_masking(request_body['cc_num'])
            if "cvv" in request_body:
                request_body["cvv"] = handle_masking(request_body['cvv'], cvv=True)
            data["log_data"] = request_body

        instance = request_log_create(data)
        return instance

    @staticmethod
    def log_response(response, instance):
        response_body = json.loads(str(response.content, "utf-8"))
        log_data = {"request": instance.id, "response_status": response.status_code, "log_data": response_body}
        response_log_create.delay(log_data)
        return log_data

    @staticmethod
    def simplify_stripe_response(response):
        """Simplify Stripe response and return"""
        data = response.data
        if "stripe_error" in data:
            response.data = {"error": data["stripe_error"]["code"]}
            response.content = json.dumps(response.data)
            return response
