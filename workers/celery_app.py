from celery import Celery

celery_app = Celery(
    'ai_studio_worker',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
)

celery_app.conf.task_routes = {
    'workers.tasks.*': {'queue': 'default'},
}
