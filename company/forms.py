from django import forms
from .models import Company
from job_seeker.models import JobApplication

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'industry_type', 'company_size', 'established_year', 'headquarters', 'website', 'contact_email', 'contact_phone', 'address', 'logo']
        exclude = ['est_date']
        widgeyts = {
            'description': forms.Textarea(attrs={"rows": 4}),
            'address': forms.Textarea(attrs={"rows": 2}),
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['status']

        