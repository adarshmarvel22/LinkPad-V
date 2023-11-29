# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
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
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("0")
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Extract additional fields
            current_year = form.cleaned_data.get('current_year')
            major = form.cleaned_data.get('major')
            print("1")
            # Create Student profile
            Student.objects.create(user_profile=UserProfile.objects.create(user=user, bio=""), current_year=current_year, major=major)
            print("2")
            messages.success(request, f'Account created for {username}!')
            return redirect('profiles:student_dashboard', username=username)
            # return render(request, 'profiles/student_dashboard.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'profiles/signup.html', {'form': form})


def login_view(request):
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

@login_required
def student_dashboard(request, username):
    user_profile = UserProfile.objects.get(user__username=username)
    return render(request, 'profiles/student_dashboard.html', {'user_profile': user_profile})

@login_required
def department_staff_dashboard(request, username):
    department_staff = DepartmentStaff.objects.get(user_profile__user__username=username)
    return render(request, 'profiles/department_staff_dashboard.html', {'department_staff': department_staff})

@login_required
def alumni_dashboard(request, username):
    alumni_profile = Alumni.objects.get(user_profile__user__username=username)
    return render(request, 'profiles/alumni_dashboard.html', {'alumni_profile': alumni_profile})
