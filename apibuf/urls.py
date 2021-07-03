from django.urls import path
from . import views
urlpatterns = [
    path('admin_registration/', views.admin_registration),
    path('foods_in_buffet/', views.foods_today),


]
