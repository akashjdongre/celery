from app.celery_app import celery_app

@celery_app.task
def add_numbers(x, y):
    print(f"Adding {x} and {y}")
    result = x + y
    print(f"Result: {result}")
    return result


@celery_app.task
def mul_numbers(x, y):
    print(f"Multiplying {x} and {y}")
    result = x * y
    print(f"Result: {result}")
    return result
