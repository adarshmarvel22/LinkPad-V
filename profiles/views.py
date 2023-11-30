# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, DepartmentStaff, Alumni, Student

def homepage(request):
    return render(request, 'profiles/homepage.html')

# profiles/views.py
from .forms import CustomUserCreationForm
# ... other imports ...

def signup(request):
    if request.user.is_authenticated:
        # If the user is already authenticated, redirect to their respective dashboard
        user_profile = request.user.userprofile

        if hasattr(user_profile, 'student'):
            return redirect('profiles:student_dashboard', username=request.user.username)
        elif hasattr(user_profile, 'departmentstaff'):
            return redirect('profiles:department_staff_dashboard', username=request.user.username)
        elif hasattr(user_profile, 'alumni'):
            return redirect('profiles:alumni_dashboard', username=request.user.username)

    user = None  # Declare the user variable outside the if block
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Extract additional fields
            current_year = form.cleaned_data.get('current_year')
            major = form.cleaned_data.get('major')
            
            # Create Student profile
            Student.objects.create(user_profile=UserProfile.objects.create(user=user, bio=""), current_year=current_year, major=major)
            
            # Log the user in
            login(request, user)

            messages.success(request, f'Account created for {username}!')
            return redirect('profiles:student_dashboard', username=username)
    else:
        form = CustomUserCreationForm()
    return render(request, 'profiles/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        # If the user is already authenticated, redirect to their respective dashboard
        user_profile = request.user.userprofile

        if hasattr(user_profile, 'student'):
            return redirect('profiles:student_dashboard', username=request.user.username)
        elif hasattr(user_profile, 'departmentstaff'):
            return redirect('profiles:department_staff_dashboard', username=request.user.username)
        elif hasattr(user_profile, 'alumni'):
            return redirect('profiles:alumni_dashboard', username=request.user.username)
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Redirect to the appropriate dashboard based on the user's role
            if hasattr(user, 'userprofile'):
                user_profile = user.userprofile

                if hasattr(user_profile, 'student'):
                    return redirect('profiles:student_dashboard', username=username)
                elif hasattr(user_profile, 'departmentstaff'):
                    return redirect('profiles:department_staff_dashboard', username=username)
                elif hasattr(user_profile, 'alumni'):
                    return redirect('profiles:alumni_dashboard', username=username)
            else:
                messages.error(request, 'Invalid user profile.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'profiles/login.html')

def logout_view(request):
    logout(request)
    return redirect('profiles:homepage')  # Redirect to your desired page after logout

@login_required
def student_dashboard(request, username):
    user_profile = UserProfile.objects.get(user__username=username)
    student_profile = Student.objects.get(user_profile=user_profile)
    return render(request, 'profiles/student_dashboard.html', {'user_profile': user_profile, 'student_profile': student_profile})

@login_required
def department_staff_dashboard(request, username):
    department_staff = DepartmentStaff.objects.get(user_profile__user__username=username)
    students = Student.objects.all()
    staff_members = DepartmentStaff.objects.exclude(user_profile__user__username=username)
    alumni_members = Alumni.objects.all()

    return render(request, 'profiles/department_staff_dashboard.html', {
        'department_staff': department_staff,
        'students': students,
        'staff_members': staff_members,
        'alumni_members': alumni_members,
    })

@login_required
def alumni_dashboard(request, username):
    alumni_profile = Alumni.objects.get(user_profile__user__username=username)
    return render(request, 'profiles/alumni_dashboard.html', {'alumni_profile': alumni_profile})

# profiles/views.py
from .forms import CustomUserCreationForm, UpdateStudentForm, AssignAlumniForm, AssignStaffForm
from django.shortcuts import get_object_or_404

@login_required
def update_student(request, username):
    user_profile = UserProfile.objects.get(user__username=username)

    # Use get_object_or_404 to handle the case where the student does not exist
    student_profile = get_object_or_404(Student, user_profile=user_profile)

    if request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student_profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student profile updated for {username}!')
            return redirect('profiles:department_staff_dashboard', username=request.user.username)
    else:
        form = UpdateStudentForm(instance=student_profile)

    return render(request, 'profiles/update_student.html', {'form': form, 'user_profile': user_profile, 'student_profile': student_profile})

@login_required
def assign_alumni(request, username):
    user_profile = UserProfile.objects.get(user__username=username)
    student_profile = Student.objects.get(user_profile=user_profile)

    if request.method == 'POST':
        alumni_form = AssignAlumniForm(request.POST, instance=Alumni(user_profile=user_profile))
        if alumni_form.is_valid():
            alumni_form.save()
            student_profile.delete()  # Remove student profile
            messages.success(request, f'{username} is now assigned as Alumni!')
            return redirect('profiles:department_staff_dashboard', username=request.user.username)
    else:
        alumni_form = AssignAlumniForm()

    return render(request, 'profiles/assign_alumni.html', {'alumni_form': alumni_form, 'user_profile': user_profile, 'student_profile': student_profile})

@login_required
def assign_staff(request, username):
    user_profile = UserProfile.objects.get(user__username=username)
    student_profile = Student.objects.get(user_profile=user_profile)

    if request.method == 'POST':
        staff_form = AssignStaffForm(request.POST, instance=DepartmentStaff(user_profile=user_profile))
        if staff_form.is_valid():
            staff_form.save()
            student_profile.delete()  # Remove student profile
            messages.success(request, f'{username} is now assigned as Department Staff!')
            return redirect('profiles:department_staff_dashboard', username=request.user.username)
    else:
        staff_form = AssignStaffForm()

    return render(request, 'profiles/assign_staff.html', {'staff_form': staff_form, 'user_profile': user_profile, 'student_profile': student_profile})

# profiles/eeletes
from django.db import IntegrityError

@login_required
def delete_staff(request, username):
    staff_member = get_object_or_404(DepartmentStaff, user_profile__user__username=username)
    staff_member.delete()
    messages.success(request, f'Staff member {username} has been deleted!')
    return redirect('profiles:department_staff_dashboard', username=request.user.username)

@login_required
def delete_alumni(request, username):
    alumni_member = get_object_or_404(Alumni, user_profile__user__username=username)
    alumni_member.delete()
    messages.success(request, f'Alumni member {username} has been deleted!')
    return redirect('profiles:department_staff_dashboard', username=request.user.username)

@login_required
def revert_to_student(request, username):
    alumni_member = get_object_or_404(Alumni, user_profile__user__username=username)

    # Extract alumni details
    graduation_year = alumni_member.graduation_year
    major = alumni_member.major

    # Check if a UserProfile already exists for the user
    existing_user_profile = UserProfile.objects.filter(user=alumni_member.user_profile.user).first()

    if existing_user_profile:
        # If UserProfile already exists, update it
        existing_user_profile.bio = ""  # Update with your logic
        existing_user_profile.save()
    else:
        # If UserProfile doesn't exist, create a new one
        try:
            student_profile = Student.objects.create(
                user_profile=UserProfile.objects.create(user=alumni_member.user_profile.user, bio=""),
                current_year=graduation_year + 1,  # You may adjust this logic based on your requirements
                major=major
            )
        except IntegrityError:
            # Handle IntegrityError if necessary
            messages.error(request, 'Error reverting to student. Please try again.')

    # Delete the Alumni profile
    alumni_member.delete()

    messages.success(request, f'{username} has been reverted to a Student!')
    return redirect('profiles:department_staff_dashboard', username=request.user.username)