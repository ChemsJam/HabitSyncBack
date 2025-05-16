from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    unit = models.CharField(max_length=20, default='minutos')  # Ej: páginas, repeticiones, horas
    target_total = models.FloatField()  # Total a lograr (ej. 300 páginas)
    days = models.JSONField()  # Ej: ["Monday", "Wednesday"]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_permanent = models.BooleanField(default=True)  # Nueva: distingue tipo
    is_completed = models.BooleanField(default=False)  # Nueva: permite marcar como terminada
    unit = models.CharField(max_length=20, default='minutos')

    def __str__(self):
        return self.title
    
class Progress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='progress')
    date = models.DateField()
    amount_done = models.FloatField()  # Por ejemplo: páginas leídas hoy
    note = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['goal', 'date']

    def __str__(self):
        return f"{self.goal.name} - {self.date}"