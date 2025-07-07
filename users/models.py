from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    verification_token = models.CharField(max_length=50, blank=True)
    is_verified = models.BooleanField(default=False)

    def generate_verification_token(self):
        self.verification_token = get_random_string(50)
        self.save()
        return self.verification_token

    def __str__(self):
        return f"{self.user.username}'s profile"