from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class UserAdmin(models.Model):
    name = models.CharField('Имя', max_length=80)
    phone = models.CharField('Номер', max_length=20)
    pin = models.CharField('ПИН', max_length=6, unique=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField('Название', max_length=255)
    mentor = models.CharField('Ментор', max_length=80, null=True, blank=True)
    assistant = models.CharField('Ассистент', max_length=80, null=True, blank=True)
    classroom = models.CharField('Номер кабинета', max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.CharField(max_length=10)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField('Имя', max_length=70)
    phone = models.CharField('Номер телефона', max_length=10, unique=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    pin = models.CharField('Пин', unique=True, max_length=8)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Buffet(models.Model):
    name = models.CharField('Наименование', max_length= 50)
    url = models.CharField(max_length=200)
    price = models.FloatField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Oper_details(models.Model):
    id_buffet = models.ForeignKey('Buffet', on_delete=models.CASCADE,)
    id_operation = models.ForeignKey('Operations', on_delete=models.CASCADE,)
    amount = models.PositiveSmallIntegerField('Количество',)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.amount


STATUS_CHOICES = [
    (True, 'Открыт'),
    (False, 'Закрыт'),
    (3, 'Списан')
]


class Operations(models.Model):
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    pin_pins = models.ForeignKey('Pin', on_delete=models.CASCADE,)
    summ = models.FloatField()
    debt_sum = models.FloatField()
    status = models.BooleanField(choices=STATUS_CHOICES,
                                 verbose_name='Статус',
                                 default=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


class Pin(models.Model):
    pin = models.CharField('Пин', max_length=6, primary_key=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pin
