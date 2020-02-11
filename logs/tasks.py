from ivr_payment.celery import app
from logs.models import ResponseLog, RequestLog


@app.task
def response_log_create(data):
    log_instance = RequestLog.objects.get(id=data['request'])
    data['request'] = log_instance
    ResponseLog.objects.create(**data)
    return {'message': 'response_log created'}


@app.task
def request_log_create(data):
    request_log = RequestLog.objects.create(**data)
    return request_log
