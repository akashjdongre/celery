from django.shortcuts import render
from myceleryproject.celery import add , multiply
from celery.result import AsyncResult

from myapp.tasks import add as add_task, multiply as multiply_task
# Create your views here.

def index(request):
    print("Result: ")

    # result1 = add_task.delay(33,44)
    # print(f"Addition Task ID : {result1}")

    result = multiply_task.delay(15,15)
    print(f"Multiplication Task ID : {result}")

    return render(request, "myapp/home.html" , {'x`result' : result})

def check_result(request, task_id):
    result = AsyncResult(task_id)
    if result.ready():
        return render(request, "myapp/result.html", context={"result": result})
    else:
        return render(request, "myapp/result.html", context={"result": "Task is still processing."})

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")