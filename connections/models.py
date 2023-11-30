# connections/models.py
from django.db import models
from django.contrib.auth.models import User

class Connection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connections')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')

    def __str__(self):
        return f'{self.user.username} - {self.friend.username}'
