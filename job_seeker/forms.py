from django import forms
from .models import JobSeeker, JobApplication

class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['profile_pic', 'full_name', 'education', 'experience', 'skills', 'resume', 'address', 'contact_number', 'linkedin', 'is_public']




class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'address', 'skills', 'education','experience', 'cover_letter', 'resume']

class JobApplicationUpdateForm(forms.ModelForm):
    class Meta:
        moddel = JobApplication
        fields = ['status', 'message']

