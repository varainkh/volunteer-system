from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Task(models.Model):
    event = models.ForeignKey(Event, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned_volunteer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Participation(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    hours_contributed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.volunteer.username} - {self.event.title}"
