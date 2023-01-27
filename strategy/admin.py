from django.contrib import admin
from .models import Instance_status2
# Register your models here.

class Admin_Instance_status(admin.ModelAdmin):
    fields = ['Pids','Pid_status','start_datetime','stop_datetime']
    model = Instance_status2

admin.site.register(Instance_status2, Admin_Instance_status)