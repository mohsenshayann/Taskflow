from .models import Task

def get_task_by_id(task_id):

    return Task.objects.get(id=task_id)

def get_user_tasks(user):

    return Task.objects.filter(project__owner=user)

def get_completed_tasks(user):

    return Task.objects.filter(project__owner=user, status="done ")
