# profiles/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class DepartmentStaff(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.department} Staff"

class Alumni(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    graduation_year = models.IntegerField()
    major = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_profile.user.username} - Alumni {self.graduation_year}"

class Student(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    current_year = models.IntegerField()
    major = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_profile.user.username} - Student {self.current_year}"
