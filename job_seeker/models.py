from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from jobs.models import Job




class JobSeeker(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    full_name = models.CharField(max_length=200)
    education = models.CharField(max_length=290)
    experience = models.CharField(max_length=300)
    skills = models.CharField(max_length=500, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=120, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.full_name
    
    


class JobApplication(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')
    full_name = models.CharField(max_length=255, default="Unknown")
    address = models.TextField(max_length=255, default="Not Provided")
    skills = models.TextField(blank=True, null=True)
    education = models.TextField(default="Not Provided")
    experience = models.TextField(blank=True, null=True)
    date_applied = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')
    message = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"Application for {self.job.title} by {self.job_seeker.user.email}"

    



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', default='default.jpg')
    application_status = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
