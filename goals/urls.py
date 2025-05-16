from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GoalViewSet, ProgressViewSet

router = DefaultRouter()
router.register(r'goals', GoalViewSet, basename='goal')
router.register(r'progress', ProgressViewSet, basename='progress')

urlpatterns = [
    path('', include(router.urls)),
]