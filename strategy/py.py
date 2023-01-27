import subprocess
from django.http import HttpResponse
import sys
import os
import psutil
import pandas as pd
from .models import Instance_status2
import datetime
import time
import schedule

def script():

    try:
        PIDA = Instance_status2.objects.values_list('Pids', flat=True)
        pid_exists_obj = psutil.pid_exists(PIDA)

        Pid_gen = datetime.datetime.now()
        print('PID for process', PIDA)
        # print(pid_exists_obj)
        # print(Pid_gen)
        # print(Db_pids1)
        Db_pids = Instance_status2.objects.values_list('Pids', 'Pid_status')
        Db_pids1 = []
        for i, j in Db_pids:
            if j == 'running':
                Db_pids1.append(i)

        for pid in Db_pids1:
            if psutil.pid_exists(pid) == False:
                # print(pid)
                Pids = pid
                Pid_status = "Stoped"
                Instance_status2.objects.filter(Pids=Pids).update(Pid_status=Pid_status)
                Pids = pid
                stop_datetime = datetime.datetime.now()
                Instance_status2.objects.filter(Pids=pid).update(stop_datetime=stop_datetime)

        if pid_exists_obj == True:
            Pid_status = 'running'
            Pid_stop = None

        return HttpResponse('Script excecuted')
    except Exception as e:

        return HttpResponse('Script not executed')
    finally:
        obj = Instance_status2(Pids=PIDA, Pid_status=Pid_status, start_datetime=Pid_gen, stop_datetime=Pid_stop)
        obj.save()


schedule.every(1).seconds.do(script)


schedule.run_pending()
