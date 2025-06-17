from django.db import models
from users.models import User


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='resumes/photos', blank=True, null=True)
    dob = models.DateField()
    contact = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    adress = models.TextField(max_length=500, blank=True, null=True)

    matriculation = models.CharField(max_length=300, blank=True, null=True)
    intermediate = models.CharField(max_length=300, blank=True, null=True)
    graduation = models.CharField(max_length=300, blank=True, null=True)
    postgraduation = models.CharField(max_length=300, blank=True, null=True)

    skills = models.TextField(max_length=500, blank=True, null=True)
    experience = models.TextField(max_length=500, blank=True, null=True)
    summary = models.TextField(max_length=500, blank=True, null=True)
    projects = models.TextField(max_length=600, blank=True, null=True)
    additional_qualifications = models.TextField(max_length=600, blank=True, null=True)
    
    
    languages = models.TextField(max_length=500, blank=True, null=True)
    hobbies = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name
                
    
