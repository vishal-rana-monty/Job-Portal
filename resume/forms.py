from django import forms
from resume.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'name',
            'photo',
            'dob',
            'contact',
            'email',
            'linkedin',
            'adress',
            'matriculation',
            'intermediate',
            'graduation',
            'postgraduation',
            'skills',
            'experience',
            'summary',
            'projects',
            'additional_qualifications',
            'languages',
            'hobbies'
        ]
        exclude = ['user']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }