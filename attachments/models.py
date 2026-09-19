from django.conf import settings
from django.db import models


class TaskAttachment(models.Model):
    task = models.ForeignKey(
        "tasks.Task",
        on_delete=models.CASCADE,
        related_name="attachments",
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="uploaded_attachments",
    )

    file = models.FileField(
        upload_to="task_attachments/%Y/%m/%d/"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

# Create your models here.
