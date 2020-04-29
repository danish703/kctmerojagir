from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee
# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    about = models.TextField(null=True,blank=True)
    profile_image = models.ImageField(upload_to='company/',null=True,blank=True)
    adress = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):return self.company_name


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='job/',null=True,blank=True)
    last_apply_date = models.DateField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(models.Model):
    cover_letter = models.TextField()
    apply_date = models.DateField()
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return self.employee

