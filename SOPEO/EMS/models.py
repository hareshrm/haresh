from django.db import models
from django.db.models import AutoField

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    leave_count = models.IntegerField(null=True, blank=True, default=0)
    on_leave = models.BooleanField(default=False)

    def __str__(self) :
        return self.name

class add(models.Model):
    department = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100,null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    priority = models.CharField(max_length=100, null=True, blank=True)
    mobile= models.CharField(max_length=100, null=True, blank=True)
    # Description= models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) :
        return self.name
    
class Admin(models.Model):
    email_id=models.EmailField()
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
