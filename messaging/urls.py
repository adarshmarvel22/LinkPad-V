# messaging/urls.py
from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('messages/', views.messages, name='messages'), 
    path('send_message/<str:target_username>/', views.send_message, name='send_message'),
    # Add other URLs as needed
]
