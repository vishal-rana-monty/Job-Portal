from django import forms
from .models import ContactQuery, Message
from users.models import User

class ContactQueryForm(forms.ModelForm):
    class Meta:
        model = ContactQuery
        fields = ['name', 'email', 'subject', 'message', 'created_at']
        exclude = ['created_at']
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message','style': 'height:150px;'}),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body', 'attachment', 'receiver']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'style': 'height:150px;'}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'receiver': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        sender = kwargs.pop('sender', None)
        super().__init__(*args, **kwargs)
        if sender.role == 'register_applicant':
            self.fields['receiver'].queryset = User.objects.filter(role='register_recruiter')
        elif sender.role == 'register_recruiter':
            self.fields['receiver'].queryset = User.objects.filter(role='register_applicnat')
