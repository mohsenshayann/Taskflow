from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskApiTest(APITestCase):

    def test_task_list(self):
        user = User.objects.create_user(username="test",password="pass123")

        self.client.force_authenticate(user=user)

        response = self.client.get(
            "/api/tasks/", follow=True
        )

        self.assertEqual(
            response.status_code,
            200
        )

