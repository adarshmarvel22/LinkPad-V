# messaging/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from profiles.models import UserProfile

@login_required
def messages(request):
    # Retrieve messages for the logged-in user
    user_messages = Message.objects.filter(recipient=request.user)

    context = {'user_messages': user_messages}
    return render(request, 'messaging/messages.html', context)

@login_required
def send_message(request, target_username):
    target_user_profile = get_object_or_404(UserProfile, user__username=target_username)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=target_user_profile.user, content=content)
            messages.success(request, f"Message sent to {target_username}.")

    return redirect('profiles:profile', username=target_username)
