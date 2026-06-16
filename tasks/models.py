
from django.db import models
from projects.models import Project
# Create your models here.

class Task(models.Model):
    
    STATUS_CHOICES = [
        ('to do', 'TO DO'),
        ('doing', 'DOING'),
        ('done', 'DONE'),
    ]
    
    project = models.ForeignKey(
    Project,
    on_delete=models.CASCADE,
    related_name='tasks'    
    )

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='todo'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
