from django.db import models
from users.models import User

# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company")
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    industry_type = models.CharField(max_length=255, null=True, blank=True)
    company_size = models.CharField(max_length=200, choices=[
        ('1-10', '1-10 Employees'),
        ('11-50', '11-50 Employees'),
        ('50-200', '50-200 Employees'),
        ('200-500', '200-500 Employees'),
        ('500+', '500+ Employees'),
    ])
    established_year = models.PositiveIntegerField(null=True, blank=True)
    headquarters = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    address = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)

    est_date = models.DateField(auto_now_add=True)


    def __str__(self): 
       return self.name