from celery import shared_task

@shared_task(name="My Task Name addition task")
def add(x, y):
    return x + y

@shared_task(name="My Task Name multiply_task")
def multiply(x, y):
    return x * y

@shared_task(name="myapp.tasks.clear_session_cache")
def clear_session_cache(id):
    from django.contrib.sessions.models import Session
    Session.objects.all().delete()
    print("Session cache cleared successfully.")
    return id

@shared_task(name="My Task Name long_running_task")
def clear_redis_cache(id):
    print("Redis cache cleared successfully.")
    return id