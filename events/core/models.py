from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    max_participants = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.date < timezone.now():
            raise ValidationError("Event date cannot be in past.")
        if self.max_participants <= 0:
            raise ValidationError("Max participants must be greater than zero.")
    def __str__(self):
        return self.title
    
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event') # prevent dupication
    
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
    
