import subprocess
from django.http import HttpResponse
import sys
import os
import psutil
import pandas as pd
from .models import Instance_status2
import datetime
from django.db.models import Case, When
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Instance_status2_serializer


if os.name == 'PID':
    def pid_exists(PID):
        import errno
        if PID < 0:
            return False
        try:
            os.kill(PID, 0)
        except OSError as e:
            return e.errno == errno.EPERM
        else:
            return True
else:
    def pid_exists(PID):
        import ctypes
        kernel32 = ctypes.windll.kernel32
        SYNCHRONIZE = 0x100000

        process = kernel32.OpenProcess(SYNCHRONIZE, 0, PID)
        if process != 0:
            kernel32.CloseHandle(process)
            return True
        else:
            return False

def check_process_status(process_name):

    process_status = [ proc for proc in psutil.process_iter() if proc.name() == process_name ]
    if process_status:
        for current_process in process_status:
            print("Process id is %s, name is %s, staus is %s"%(current_process.pid, current_process.name(), current_process.status()))
    else:
        print("Process name not valid", process_name)

def script1(r):
    try:
        obj = subprocess.Popen([sys.executable,'strategy//scripts//script1.py'])
        PID = obj.pid
        print('PID for process', PID)
        print(pid_exists(PID))
        print(check_process_status(r))
        return HttpResponse('Script excecuted')
    except Exception as e:
        print("Error while starting script", e)
        return HttpResponse('Script not executed')



def script2(r):
    try:
        obj = subprocess.Popen([sys.executable,'strategy//scripts//test2.py'])
        PID = obj.pid
        print('PID for process', PID)
        print(psutil.Process(PID))
        return HttpResponse('Script excecuted')
    except Exception as e:
        print(psutil.pid_exists(PID),"|",e)
        return HttpResponse('Script not executed')

def script3(r):
    try:
        obj = subprocess.Popen([sys.executable, 'strategy//scripts//script3.py'])
        PIDA =obj.pid
        pid_exists_obj = psutil.pid_exists(PIDA)

        Pid_gen = datetime.datetime.now()
        print('PID for process', PIDA)
        #print(pid_exists_obj)
        #print(Pid_gen)
        #print(Db_pids1)
        Db_pids = Instance_status2.objects.values_list('Pids', 'Pid_status')
        Db_pids1 = []
        for i,j in Db_pids:
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
                Instance_status2.objects.filter(Pids=pid).update(stop_datetime = stop_datetime)



        if pid_exists_obj == True:
            Pid_status = 'running'
            Pid_stop = None


        return HttpResponse('Script excecuted')
    except Exception as e:


        return HttpResponse('Script not executed')
    finally:
        obj = Instance_status2(Pids = PIDA,Pid_status=Pid_status,start_datetime=Pid_gen,stop_datetime = Pid_stop)
        obj.save()

@api_view(['GET'])
def Instance_status(r):
    getstrategy = Instance_status2.objects.all()
    serializer = Instance_status2_serializer(getstrategy,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

