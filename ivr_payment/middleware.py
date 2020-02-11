import json


class CustomMiddleware(object):
    """Logs all REQUEST and RESPONSE made to/from the middleware application"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        request_log = self.log_request(request)
        response = self.get_response(request)
        self.log_response(response, request_log)
        return response

    @classmethod
    def log_request(cls, request):
        log_data = {"request_type": request.method, "url_path": request.get_full_path()}

        if not request.body:
            from logs.exceptions import RequestWithoutData
            raise RequestWithoutData

        request_body = json.loads(str(request.body, 'utf-8'))

        if "cc_num" in request_body:
            request_body["cc_num"] = cls.handle_masking(request_body['cc_num'])
        if "cvv" in request_body:
            request_body["cvv"] = cls.handle_masking(request_body['cvv'], cvv=True)

        log_data["log_data"] = request_body

        from logs.models import RequestLog
        return RequestLog.objects.create(**log_data)

    @staticmethod
    def log_response(response, instance):
        response_body = json.loads(str(response.content, 'utf-8'))
        log_data = {"request": instance, "response_status": response.status_code, "log_data": response_body}

        from logs.models import ResponseLog
        return ResponseLog.objects.create(**log_data)

    @staticmethod
    def handle_masking(item, cvv=False):
        return ("*" * len(item)) if cvv else "*" * (len(item) - 4) + item[-4:]
