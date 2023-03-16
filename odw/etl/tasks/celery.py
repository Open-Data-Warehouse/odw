from celery import Celery

REDIS_HOST = "redis"
REDIS_PORT = 6379

BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
BACKEND_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/1"

app = Celery("tasks", broker=BROKER_URL, backend=BACKEND_URL, include=["odw.etl.tasks"])
app.autodiscover_tasks(packages=['odw.etl.tasks'])