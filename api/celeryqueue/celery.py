import os

from celery import Celery

CELERY_BROKER_URL = (
    os.environ.get("CELERY_BROKER_URL", "amqp://rabbitmq:rabbitmq@rabbit:5672"),
)
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "rpc://")


celery = Celery("loan", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
