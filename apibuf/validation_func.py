from .models  import UserAdmin, Pin
from rest_framework import serializers
from django.db.models import Count, Q
import datetime



def unique_pin_db_pin(pin):
    pins_in_db = Pin.objects.filter(pin=pin).last()
    if pins_in_db:
        raise serializers.ValidationError(['Should be unique'])


