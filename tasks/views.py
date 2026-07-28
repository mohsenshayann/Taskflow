import logging
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend


from .models import Task
from .serializers import TaskSerializer

from .services import TaskService

logger = logging.getlogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter              
    ]
    
    filterset_fields = ['status']
    search_fields = ['title', 'descriptions']
    ordering_fields = ['created_at', 'title']
    
    def get_queryset(self):
        queryset = Task.objects.filter(project__owner=self.request.user)
        logger.debug(f"User {self.request.user} fetched {queryset.count()} tasks")
        return queryset

    def perform_create(self, serializer):

        data = serializer.validated_data

        TaskService.create_task(
            project=data["project"],
            title=data["title"],
            description=data.get("description", "")
            status=data.get("status", "todo")
        )