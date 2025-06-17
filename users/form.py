




from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User
from django import forms
from django.core.exceptions import ValidationError

class RegisterUserForm(UserCreationForm):
    # full_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'})
    )
    

    class Meta:
        model = get_user_model()
        fields = ['email','full_name', 'phone_number',  'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        role = self.data.get('role')
        if User.objects.filter(email=email, role=role).exists():
            raise forms.ValidationError(f"User with this email already exists as {role}.")
        return email
    def clean_password1(self):
        password = self.cleaned_data.get("password1")

        errors = []
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in password):
            errors.append("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password):
            errors.append("Password must contain at least one lowercase letter.")
        if not any(char.isdigit() for char in password):
            errors.append("Password must contain at least one number.")
        if not any(char in "!@#$%^&*()" for char in password):
            errors.append("Password must contain at least one special character (!@#$%^&*()).")

        if errors:
            raise ValidationError(errors)

        return password
    

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Confirm Password is not match. Plese Enter the same password")
        
        return password2