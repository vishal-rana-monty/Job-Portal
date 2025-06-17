
from django.db import models
from django.conf import settings
from users.models import User
from company.models import Company


# Create your models here.
class Skill(models.Model):
    skill_name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.skill_name 
    

class JobCategory(models.Model):
    name = models.CharField(max_length=200, unique=False)
    icon = models.CharField(max_length=200, default="fa fa-building")

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=200)
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs", null=True, blank=True)
    company_name = models.CharField(max_length=100,null=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_type = models.CharField(max_length=100, unique=False)
    experience_required = models.CharField(help_text="Experience in years",max_length=200,choices=[
        ('0-2', '0-2 Years'),
        ('2-4', '2-4 Years'),
        ('4-6', '4-6 Years'),
        ('6-8', '6-8 Years'),
        ('8+', '8+ Years'),
    ])
    skills = models.ManyToManyField(Skill, related_name="jobs") 
    company_website = models.URLField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name="jobs", null=True, blank=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return self.title
    

class JobApplicationModel(models.Model):
    job_seeker = models.ForeignKey(
        f"{settings.JOB_SEEKER_APP}.JobSeeker",  # Use string reference
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
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
    
class SavedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
