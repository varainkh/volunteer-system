from django.db import models
from django.contrib.auth.models import User

class VolunteerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='volunteer_profile')
    contact_info = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    total_hours = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
