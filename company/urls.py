from django.urls import path
from . import views
urlpatterns=[
    path('register/',views.register,name='company_register'),
    path('dashboard/',views.dashbaord,name='dashboard'),
    path('edit-company/',views.edit_company,name='edit_company'),
    path('post-job',views.createjob,name='postjob'),
    path('vacancylist',views.vacancylist,name='vacancylist'),
    path('edit-job/<int:id>',views.editjob,name='editjob'),
    path('delete-job/<int:id>',views.removejob,name='removejob'),
]