from rest_framework import serializers

from .models import TaskAttachment


class TaskAttachmentSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TaskAttachment
        fields = [
            "id",
            "task",
            "uploaded_by",
            "file",
            "created_at",
        ]
        read_only_fields = [
            "uploaded_by",
            "created_at",
        ]

    def validate_file(self, value):
        max_size = 10 * 1024 * 1024

        if value.size > max_size:
            raise serializers.ValidationError(
                "File size cannot exceed 10 MB."
            )

        allowed_extensions = {
            ".pdf",
            ".png",
            ".jpg",
            ".jpeg",
            ".doc",
            ".docx",
        }

        extension = value.name.lower().rsplit(".", 1)[-1]
        extension = f".{extension}"

        if extension not in allowed_extensions:
            raise serializers.ValidationError(
                "Unsupported file type."
            )

        return value