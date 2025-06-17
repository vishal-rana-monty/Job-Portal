from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
      email = self.cleaned_data.get('email')
      try:
         user = User.objects.filter(email=email).first()
      except User.DoesNotExist:
         raise forms.ValidationError("No user found with this email.")
      return email
