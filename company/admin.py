from django.contrib import admin
from .models import Company,Job,Application
# Register your models here.
admin.site.register([Company,Job,Application])
