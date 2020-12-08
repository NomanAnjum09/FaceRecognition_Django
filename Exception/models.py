from django.db import models
from django.utils import timezone

# Create your models here.

class Exception(models.Model):
    exception_number = models.IntegerField()
    message = models.CharField(max_length=200)
    timeStamp = models.DateTimeField()
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.timeStamp = timezone.now()
        return super(Exception, self).save(*args, **kwargs)
    def __str__(self):
        return self.exception_number
