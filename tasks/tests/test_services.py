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


#### tasks/tests/test_services.py
#import pytest
#from django.contrib.auth import get_user_model
#from tasks.services import TaskService
#from tasks.models import Task

#User = get_user_model()


#@pytest.mark.django_db
#def test_create_task():
#   user = User.objects.create_user(username="alex", password="123")

#    data = {
#        "title": "pytest task",
#        "description": "test"
#    }

#    task = TaskService.create_task(user, data)

#    assert task.title == "pytest task"
#    assert Task.objects.count() == 1