# connections/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Connection
from profiles.models import UserProfile

@login_required
def send_connection_request(request, target_username):
    target_user_profile = get_object_or_404(UserProfile, user__username=target_username)

    # Check if a connection already exists
    existing_connection = Connection.objects.filter(user=request.user, friend=target_user_profile.user)
    if existing_connection.exists():
        messages.info(request, f"You are already connected with {target_username}.")
        return redirect('profiles:profile', username=target_username)

    Connection.objects.create(user=request.user, friend=target_user_profile.user)
    messages.success(request, f"Connection request sent to {target_username}.")
    return redirect('profiles:profile', username=target_username)
