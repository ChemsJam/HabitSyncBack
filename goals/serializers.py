from rest_framework import serializers
from .models import Goal, Progress

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'goal', 'date', 'amount_done', 'note']
        
class GoalSerializer(serializers.ModelSerializer):
    progress = ProgressSerializer(many=True, read_only=True)

    class Meta:
        model = Goal
        fields = [
            'id', 'user', 'name', 'description', 'category',
            'unit', 'target_total', 'days',
            'is_permanent', 'is_completed',
            'created_at', 'progress'
        ]
        read_only_fields = ['user']

    def validate(self, data):
        is_permanent = data.get('is_permanent')
        target_total = data.get('target_total')

        if is_permanent and target_total is not None:
            raise serializers.ValidationError("Las metas permanentes no deben tener un objetivo total.")
        if not is_permanent and target_total is None:
            raise serializers.ValidationError("Las metas no permanentes deben tener un objetivo total.")
        return data

