from rest_framework import viewsets, permissions
from .models import Goal, Progress
from .serializers import GoalSerializer, ProgressSerializer 
from django.shortcuts import get_object_or_404

# Create your views here.
class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class ProgressViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Progress.objects.filter(goal__user=self.request.user)