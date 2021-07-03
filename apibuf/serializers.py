from rest_framework import serializers
from .models import (UserAdmin,
                     Buffet,
                     Operations)
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


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = '__all__'