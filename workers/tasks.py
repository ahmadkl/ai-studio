from workers.celery_app import celery_app

@celery_app.task(name='workers.tasks.generate_image_task')
def generate_image_task(prompt: str):
    return {"status": "queued", "prompt": prompt}

@celery_app.task(name='workers.tasks.generate_video_task')
def generate_video_task(prompt: str, duration_seconds: int = 10):
    return {"status": "queued", "prompt": prompt, "duration_seconds": duration_seconds}
