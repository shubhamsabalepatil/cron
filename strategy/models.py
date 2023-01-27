from django.db import models

# Create your models here.
class Instance_status2(models.Model):
    Pids = models.IntegerField()
    Pid_status = models.CharField(max_length=30)
    start_datetime = models.DateTimeField(null=False)
    stop_datetime = models.DateTimeField(default=None)

