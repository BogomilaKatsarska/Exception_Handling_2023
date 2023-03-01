import logging
from celery import shared_task
import time
import logging


@shared_task
def send_welcome_emails_to_new_users():
    time.sleep(7)
    logging.info("Email was sent.")
