from django.db.models import Count, Q

from projects.models import Project
from tasks.models import Task
from notifications.model import Activity


class DashboardService:

    @staticmethod
    def get_user_dashboard(user):
        projects = Project.objects.filter(
            memberships__user=user
        ).distinct()

        tasks = Task.objects.filter(
            project__in=projects
        )

        activities = Activity.objects.filter(
            project__in=projects
        ).select_related(
            "user",
            "project",
        ).order_by("-created_at")[:5]

        return {
            "projects_count": projects.count(),
            "tasks_count": tasks.count(),

            "completed_tasks": tasks.filter(
                status="completed"
            ).count(),

            "pending_tasks": tasks.exclude(
                status="completed"
            ).count(),

            "recent_tasks": tasks.select_related(
                "project"
            ).order_by("-created_at")[:5],
        }