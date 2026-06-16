from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend


from .models import Task
from .serializers import TaskSerializer


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
        return Task.objects.filter(
            project__owner=self.request.user
        )