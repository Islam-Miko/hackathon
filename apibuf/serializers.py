from rest_framework import serializers
from .models import (UserAdmin,
                     Buffet,
                     Operations,
                    Oper_details,
                     Pin)

from .validation_func import unique_pin_db_pin
class UserAdminSerizalier(serializers.Serializer):
    name = serializers.CharField(max_length=50, min_length=1)
    phone = serializers.CharField(min_length=10, max_length=10)
    pin = serializers.CharField(min_length=6, max_length=8,
                                validators=[unique_pin_db_pin])

class BuffetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buffet
        exclude = ('active', )

class PinSerializer(serializers.Serializer):
    pin = serializers.CharField(max_length=8, min_length=6)

    def create(self, validated_data):
        return Pin.objects.create(validated_data)


class OperationSerializer(serializers.Serializer):
    summ = serializers.FloatField()
    debt_sum = serializers.FloatField()
    pin_pins = PinSerializer()

class SubOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oper_details
        fields = '__all__'