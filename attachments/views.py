from rest_framework import permissions, viewsets

from .models import TaskAttachment
from .serializers import TaskAttachmentSerializer


class TaskAttachmentViewSet(viewsets.ModelViewSet):
    serializer_class = TaskAttachmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TaskAttachment.objects.filter(
            task__project__members=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            uploaded_by=self.request.user
        )
# Create your views here.
