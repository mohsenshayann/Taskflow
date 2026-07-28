from .models import Task
from .exceptions import TaskLimitReached

import logging

logger = logging.getlogger(__name__)

class TaskService:

    @staticmethod
    def create_task(
        project,
        title,
        description=""
        status="todo"
    ):

        if project.task.count() >= 100:
            raise TaskLimitReached()

        task = Task.objects.create(
            project=project,
            title=title,
            description=description
        )

        logger.info(
            f"Task created: {task.id}"
        )

        return task

    @staticmethod
    def delete_task(task):

        task_id = task.id

        task.delete()

        logger.info(
            f"Task deleted: {task_id}"
        )

        return True