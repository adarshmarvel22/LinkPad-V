# profiles/urls.py
from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('student/<str:username>/', views.student_dashboard, name='student_dashboard'),
    path('department-staff/<str:username>/', views.department_staff_dashboard, name='department_staff_dashboard'),
    path('alumni/<str:username>/', views.alumni_dashboard, name='alumni_dashboard'),
]
