from django.urls import path
from . import views
urlpatterns=[
    path('register/',views.register,name='company_register'),
    path('dashboard/',views.dashbaord,name='dashboard')
]