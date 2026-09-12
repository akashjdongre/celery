from app.tasks import add_numbers , mul_numbers
 
print("Sending Addition Task to Celery...")

task = add_numbers.delay(10, 20)

print("Addition Task Task sent!")
print("Addition Task ID:", task.id)

print("Sending Multiplication Task to Celery...")

task = mul_numbers.delay(10, 20)

print("Multiplication Task Task sent!")
print("Multiplication Task ID:", task.id)