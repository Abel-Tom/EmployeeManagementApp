from zelthy.apps.dynamic_models.models import DynamicModelBase
from zelthy.apps.dynamic_models.fields import ZForeignKey
from zelthy.apps.dynamic_models.fields import ZOneToOneField
from django.contrib.auth.models import User
from django.db import models

class Employee(DynamicModelBase):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('transgender', 'Transgender'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    years_of_experience = models.IntegerField(default=0)
    time_off_days = models.IntegerField(default=12) # Employees get 12 days off per year
    termination_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 

    
