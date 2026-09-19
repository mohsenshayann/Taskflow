import pytest


@pytest.mark.django_db
def test_dashboard_requires_authentication(api_client):
    response = api_client.get("/api/dashboard/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_dashboard_returns_user_data(api_client, user):
    api_client.force_authenticate(user=user)

    response = api_client.get("/api/dashboard/")

    assert response.status_code == 200
    assert "projects_count" in response.data
    assert "tasks_count" in response.data
# Create your tests here.
