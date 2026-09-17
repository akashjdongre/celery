from celery import shared_task

@shared_task(name="add_task")
def add(x, y):
    return x + y

@shared_task(name="multiply_task")
def multiply(x, y):
    return x * y

@shared_task(name="clear_session_cachetask")
def clear_session_cache(id):
    from django.contrib.sessions.models import Session
    Session.objects.all().delete()
    print("Session cache cleared successfully.")
    return id