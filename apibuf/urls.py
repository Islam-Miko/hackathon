from django.urls import path
from . import views
urlpatterns = [
    path('admin_registration/', views.admin_registration),
    path('admin_authentication', views.admin_authentication),
    path('foods_in_buffet/', views.foods_today),
    path('operations', views.create_operation)


]
