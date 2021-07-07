from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/read/', CourseListView.as_view(), name='course_read'),
    path('course/update/<int:pk>/', CourseDetailView.as_view(), name='course_update'),
    path('buffet/create/', BuffetCreateView.as_view(), name='buffet_create'),
    path('buffet/read/', BuffetListView.as_view(), name='buffet_read'),
    path('buffet/update/<int:pk>/', BuffetDetailView.as_view(), name='buffet_update'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/read/', StudentListView.as_view(), name='student_read'),
    path('students/update/<int:pk>/', StudentDetailView.as_view(), name='student_update'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/read/', UserListView.as_view(), name='user_read'),
    path('users/update/<int:pk>', UserDetailView.as_view(), name='user_update'),

]


