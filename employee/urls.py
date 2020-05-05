from django.urls import path
from . import views
urlpatterns = [
   path('register/',views.registeremployee,name='registeremployee')
]