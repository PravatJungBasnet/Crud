from .models import Student
from django import forms
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','password']
        widgets={'required':forms.PasswordInput}