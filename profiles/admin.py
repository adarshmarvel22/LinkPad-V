# profiles/admin.py
from django.contrib import admin
from .models import UserProfile, DepartmentStaff, Alumni, Student

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')

@admin.register(DepartmentStaff)
class DepartmentStaffAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'department', 'position')

@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'graduation_year', 'major')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'current_year', 'major')
