from .models import Exception

def save_exception_to_db(message):
    last = Exception.objects.all().last()
    if last:
        number = last.exception_number
    else:
        number = 1
    Exception.objects.create(exception_number = number,message=message)