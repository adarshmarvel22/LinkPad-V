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
    path('update-student/<str:username>/', views.update_student, name='update_student'),
    path('assign_alumni/<str:username>/', views.assign_alumni, name='assign_alumni'),
    path('assign_staff/<str:username>/', views.assign_staff, name='assign_staff'),

    path('delete_staff/<str:username>/', views.delete_staff, name='delete_staff'),
    path('delete_alumni/<str:username>/', views.delete_alumni, name='delete_alumni'),
    path('revert_to_student/<str:username>/', views.revert_to_student, name='revert_to_student'),

    path('logout/', views.logout_view, name='logout'),

    path('clubs/', views.clubs, name='clubs'),
    path('notices/', views.notices, name='notices'),
    path('events/', views.events, name='events'),
    path('alumni_stories/', views.alumni_stories, name='alumni_stories'),
    path('internship_jobs/', views.internship_jobs, name='internship_jobs'),
    path('discussion_forums/', views.discussion_forums, name='discussion_forums'),
]
