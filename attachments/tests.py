from django.core.files.uploadedfile import SimpleUploadedFile
import pytest


@pytest.mark.django_db
def test_upload_attachment(api_client, user, task):
    api_client.force_authenticate(user=user)

    file = SimpleUploadedFile(
        "test.pdf",
        b"fake pdf content",
        content_type="application/pdf",
    )

    response = api_client.post(
        "/api/attachments/",
        {
            "task": task.id,
            "file": file,
        },
        format="multipart",
    )

    assert response.status_code == 201
# Create your tests here.
