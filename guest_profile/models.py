from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Logged in as {self.user.username} "
            f"({self.user.first_name} {self.user.last_name})"
        )
