import logging
from celery import shared_task

logger = logging.getlogger(__name__)

@shared_task
def send_welcome_email(email):

    logger.info(f"sending welcome email to {email}")
    try:

        print(f"welcome email sent to {email}")
        logger.info(f"welcome email successfully sent to {email}")
        return True
    
    except Exception as e:
        logger.error(f"Failed to send welcome email to {email}: {e}")
        raise