from rest_framework import serializers


class CreditCardSerializer(serializers.Serializer):
    cc_num = serializers.IntegerField()
    cvv = serializers.IntegerField()
    exp_date = serializers.CharField(max_length=128)
    trans_id = serializers.IntegerField()

    @staticmethod
    def validate_cvv(attrs):
        if 2 > attrs > 4:
            from logs.exceptions import InvalidCVV
            raise InvalidCVV
        return attrs

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
