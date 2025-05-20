from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Goal, Progress
from .serializers import GoalSerializer, ProgressSerializer
from rest_framework import status

# Create your views here.
class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
     # Acción personalizada para marcar meta como completada
    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        goal = self.get_object()

        if goal.is_completed:
            return Response({"detail": "La meta ya está completada."}, status=status.HTTP_400_BAD_REQUEST)

        goal.is_completed = True
        goal.save()
        return Response({"detail": "Meta marcada como completada."}, status=status.HTTP_200_OK)
        
class ProgressViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Progress.objects.filter(goal__user=self.request.user)