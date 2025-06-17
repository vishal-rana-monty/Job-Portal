from django import forms
from .models import Job, JobApplicationModel, Skill

class JobForm(forms.ModelForm):
    



    class Meta:
        model = Job
        fields = ['category','title', 'company_name', 'description', 'location', 'salary', 'job_type', 'experience_required', 'skills','company_website','created_at', 'updated_at']
        exclude = ['created_at', 'updated_at']
        widgets = {
            'skills': forms.SelectMultiple(attrs={
                'class': 'js-skill-select form-control',
                'multiple' : 'miltiple' # Important! 
            }),
        }
        

    

    def __init__ (self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select a Category"
        self.fields['experience_required'].empty_label = "Select Experience"
        self.fields['company_name'] = forms.CharField(
            label="Company Name", 
            required=False, 
            initial='', 
            widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'})
        )

class JobApplicationModelForm(forms.ModelForm):
    class Meta:
        model = JobApplicationModel
        fields = ['full_name', 'address', 'skills', 'education', 'cover_letter', 'resume']

class JobApplicationUpdateForm(forms.ModelForm):
    class Meta:
        model = JobApplicationModel
        fields = ['status', 'message']