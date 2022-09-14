from rest_framework import serializers


class CardSerializer(serializers.Serializer):
    card_name = serializers.CharField(required=True)
    task_instance = serializers.JSONField(required=False)


class TaskItemSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)


class DoneTaskSerializer(serializers.Serializer):
    is_pending = serializers.BooleanField()
