import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def User():
    return User.object.create_user(
        username="alex",
        password="1234"
    )