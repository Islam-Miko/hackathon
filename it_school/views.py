from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseDetailSerializers
    queryset = Course.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )


class CourseCreateView(generics.CreateAPIView):
    serializer_class = CourseDetailSerializers


class CourseListView(generics.ListAPIView):
    serializer_class = CourseListSerializers
    queryset = Course.objects.all()
    # permission_classes = (IsAuthenticated, )


class BuffetDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuffetDetailSerializers
    queryset = Buffet.objects.all()
    # permission_classes = (IsOwnerOrReadOnly,)


class BuffetCreateView(generics.CreateAPIView):
    serializer_class = BuffetDetailSerializers


class BuffetListView(generics.ListAPIView):
    serializer_class = BuffetListSerializers
    queryset = Buffet.objects.all()
    # permission_classes = (IsAuthenticated,)


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerializers
    queryset = Students.objects.all()
    # permission_classes = (IsOwnerOrReadOnly,)


class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentDetailSerializers


class StudentListView(generics.ListAPIView):
    serializer_class = StudentListSerializers
    queryset = Students.objects.all()
    # permission_classes = (IsAuthenticated,)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializers
    queryset = UserAdmin.objects.all()
    # permission_classes = (IsOwnerOrReadOnly,)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializers


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializers
    queryset = UserAdmin.objects.all()
    # permission_classes = (IsAuthenticated,)


def index(request):
    return render(request, template_name='it_school/index.html')
