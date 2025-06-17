from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Admin = 'admin'
    Recruiter = 'register_recruiter'
    Applicant = 'register_applicant'

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('register_recruiter', 'Recruiter'),
        ('register_applicant', 'Applicant'),
    ]



    role = models.CharField(max_length=50,choices=ROLE_CHOICES,default='Applicant')
    email = models.EmailField()
    full_name = models.CharField(max_length=200)
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)


    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)

    
    

    class Meta:
        unique_together = ('email','role')


    def __str__(self):
         return f"{self.email} ({self.role})"
    
# class Profile