# profiles/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Add this line to import the User model

class CustomUserCreationForm(UserCreationForm):
    current_year = forms.IntegerField(label='Current Year')
    major = forms.CharField(max_length=100, label='Major')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('current_year', 'major')

# profiles/UpdateStudentForm.py
from .models import Student, Alumni, DepartmentStaff

class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['current_year', 'major']

class AssignAlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['graduation_year', 'major']

class AssignStaffForm(forms.ModelForm):
    class Meta:
        model = DepartmentStaff
        fields = ['department', 'position']
