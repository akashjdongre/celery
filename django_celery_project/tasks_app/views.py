from django.http import JsonResponse
from .tasks import add

def trigger_task(request):
    result = add.delay(14, 16)
    return JsonResponse({'task_id': result.id, 'status': 'Task submitted'})