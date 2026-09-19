from rest_framework.routers import DefaultRouter

from .views import TaskAttachmentViewSet


router = DefaultRouter()

router.register(
    "attachments",
    TaskAttachmentViewSet,
    basename="attachment",
)

urlpatterns = router.urls