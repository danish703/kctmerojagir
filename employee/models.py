from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    highest_education = models.CharField(max_length=50,null=True,blank=True)
    professional_title = models.CharField(max_length=100)
    about = models.TextField(null=True,blank=True)
    profile_image = models.ImageField(upload_to='employee/',null=True,blank=True)
    resume = models.FileField(upload_to='resume/')
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Skill(models.Model):
    title = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):return self.title