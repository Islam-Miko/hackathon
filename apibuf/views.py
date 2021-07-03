
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserAdminSerizalier
from .models import UserAdmin
from .auxilary_functions import (create_user_admin,
                                create_pin_in_pinDB,
                                make_pin, get_all_active_foods
                                )

@api_view(['POST'])
def admin_registration(request):
    if request.method == 'POST':
        phone = request.data.get('phone')
        pin = make_pin(phone)
        request.data['pin'] = pin
        serializer = UserAdminSerizalier(data=request.data)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data['name']
            phone = serializer.validated_data['phone']
            valid_pin = serializer.validated_data['pin']
        create_pin_in_pinDB(valid_pin)
        create_user_admin(name=name, phone=phone, pin=valid_pin)
        return Response(pin, status=status.HTTP_201_CREATED)


@api_view('GET')
def foods_today(request):
    all_foods = get_all_active_foods()





