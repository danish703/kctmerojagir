from django.urls import path
from . import views
urlpatterns = [
   path('register/',views.registeremployee,name='registeremployee'),
   path('edit-employee/', views.edit_employee, name='edit_employee'),
   path('dashboard/',views.dashbaord,name='emp_dashbaord'),
   path('skill-remove/<int:id>/',views.removeskill,name='remove_skill')
]