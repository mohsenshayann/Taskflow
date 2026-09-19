from .models import Notification
from .models import activity
from notifications.services import ActivityService

ActivityService.create_activity(
    project=task.project,
    user=user,
    action="task_created",
    description=f'{user.username} created task "{task.title}"',
)

class NotificationService:

    @staticmethod
    def create_notification(recipient, message):
        return Notification.objects.create(
            recipient=recipient,
            message=message,
        )

class ActivityService:

    @staticmethod
    def create_activity(project, user, action, description):
        return Activity.objects.create(
            project=project,
            user=user,
            action=action,
            description=description,
        )