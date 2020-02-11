from django.db import models
from django_mysql.models import Model, JSONField


class BaseLog(Model):
    created_at = models.DateTimeField(auto_now_add=True)
    log_data = JSONField(null=True)

    class Meta:
        abstract = True


class RequestLog(BaseLog):
    request_type = models.CharField(max_length=128)
    url_path = models.CharField(max_length=255)


class ResponseLog(BaseLog):
    request = models.ForeignKey('RequestLog', on_delete=models.CASCADE, related_name='responses')
    response_status = models.PositiveIntegerField()
