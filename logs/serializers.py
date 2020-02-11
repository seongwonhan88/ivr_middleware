from rest_framework import serializers


class CreditCardSerializer(serializers.Serializer):
    cc_num = serializers.IntegerField()
    cvv = serializers.CharField()
    exp_date = serializers.CharField(max_length=128)
    trans_id = serializers.IntegerField()
