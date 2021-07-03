from .models import UserAdmin, Pin, Buffet


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