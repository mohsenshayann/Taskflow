import logging
from rest_framework.exceptions import APIException

logger = logging.getLogger(__name__)

class TaskLimitReached(
    APIException
):

    status_code = 400

    default_detail = (
        "Task limit reached"
    )