from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    target_minutes = models.PositiveIntegerField()
    days = models.JSONField()  # Ej: ["Monday", "Wednesday"]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Progress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='progress')
    date = models.DateField()
    minutes_done = models.PositiveIntegerField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['goal', 'date']

    def __str__(self):
        return f"{self.goal.name} - {self.date}"