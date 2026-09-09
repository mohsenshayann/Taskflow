from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class TaskAPITest(APITestCase)

    def setUp(self):
        self.user = User.objects.create_user(
            username="alex",
            password="123456"
        )

self.token = Token.objects.create(user=self.user)
self.client.credentials(
    HTTP_AUTHORIZATION='Token ' + self.token.key
)
 def test_create_task(self):
    url = "/api/tasks/"

    data = {
        "title": "API Task",
        "description": "API Desc"
    }

response = self.client.post(url, data)

self.assertEqual(response.status_code, 201)
self.assertEqual(response.data["title"], "API Task")


#@pytest.mark.django_db
#def test_create_task_api(client, user):
 #   client.force_login(user)

#    response = client.post("/api/tasks/", {
 #       "title": "API pytest"
  #  })

   # assert response.status_code == 201