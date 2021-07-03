from .models import UserAdmin, Pin, Buffet
from .serializers import SubOperationSerializer

def create_user_admin(name, phone, pin):
    new_user = UserAdmin.objects.create(name=name, phone=phone, pin=pin)
    new_user.save()

def create_pin_in_pinDB(pin):
    new_pin = Pin.objects.create(pin=pin)
    new_pin.save()

def make_pin(phone):
    pin = phone[4:]
    pin_in_DB = Pin.objects.filter(pin=pin).last()
    if pin_in_DB:
        return phone[3:]
    else:
        return pin

def get_all_active_foods():
    all_active_foods = Buffet.objects.filter(active=True).all()
    return all_active_foods


def get_student(operation):
    pin = operation.pop('pin_pins')
    Student = Pin.objects.filter(pin=pin).last()
    return Student

class NoUserError(Exception):
    ...
def get_userAdmin(data):
    user_admin = UserAdmin.objects.filter(phone=data['userPhone']).last()
    if user_admin is None:
        raise NoUserError
    return user_admin


def create_suboper_details(operation, suboperations):
    for sub_oper in suboperations:
        serializer = SubOperationSerializer(sub_oper)