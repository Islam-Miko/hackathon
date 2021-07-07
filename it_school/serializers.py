from rest_framework import serializers
from .models import *


class CourseListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = '__all__'


class BuffetListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buffet
        fields = '__all__'


class BuffetDetailSerializers(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Buffet
        fields = '__all__'


class StudentListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class StudentDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Students
        fields = '__all__'


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAdmin
        fields = '__all__'


class UserDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserAdmin
        fields = '__all__'


