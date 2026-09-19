from rest_framework import serializers
from .models import Notification,Activity


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "message",
            "is_read",
            "created_at",
        ]
        read_only_fields = fields

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Activity
        fields = [
            "id",
            "user",
            "action",
            "description",
            "created_at",
        ]