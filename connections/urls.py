# connections/urls.py
from django.urls import path
from . import views

app_name = 'connections'

urlpatterns = [
    path('send_connection_request/<str:target_username>/', views.send_connection_request, name='send_connection_request'),
    # Add other URLs as needed
]
