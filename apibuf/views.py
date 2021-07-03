from .exceptions import NoUserError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserAdminSerizalier, BuffetSerializer, OperationSerializer
from .models import UserAdmin
from .auxilary_functions import (create_user_admin,
                                create_pin_in_pinDB,
                                make_pin, get_all_active_foods,
                                get_student,
                                create_suboper_details, get_userAdmin,
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


@api_view(['POST'])
def admin_authentication(request):
    data = request.data
    try:
        user_name = get_userAdmin(data)
        if user_name.pin == data['userPin']:
            return Response(True, status=status.HTTP_200_OK)
        else:
            return Response('Неверные данные', status=status.HTTP_400_BAD_REQUEST)
    except NoUserError:
        return Response('Пользователь не найден в системе ', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def foods_today(request):
    all_foods = get_all_active_foods()
    serializer = BuffetSerializer(all_foods, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_operation(request):
    operation = request.data
    student = get_student(operation)
    operation['pin_pins'] = student
    sub_operations = operation.pop('oper_details')
    if request.method == 'POST':
        operations = OperationSerializer(operation)
        if operations.is_valid(raise_exception=True):
            operations.save()
        create_suboper_details(operations, sub_operations)
        return Response(operations.data)






