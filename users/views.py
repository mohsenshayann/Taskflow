from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from tasks.tasks import send_welcome_email


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        send_welcome_email.delay(user.email)

# Create your views here.
