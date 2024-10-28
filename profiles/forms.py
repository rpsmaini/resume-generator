from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'job_position', 'contact_number', 'email', 'linkedin', 'address', 'location', 'skills']
