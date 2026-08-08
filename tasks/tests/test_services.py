from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.services import TaskService
from tasks.model import Task

User = get_user_model()

class TaskServiceTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="alex",
            password="123456"

        )

def test_create_task(self):
    data = {
        "title": "Test Task",
        "description": "Test Desc"
    }

task = Task_Service.create_task(self.user,data)

self.assertEqual(task.title, "Test Task")
self.assertEqual(task.user, self.user)
self.assertEqual(Task.object.count(), 1)