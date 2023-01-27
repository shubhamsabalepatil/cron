import subprocess
import sys

def run():
    obj = subprocess.Popen([sys.executable,'strategy//scripts//script3.py'])
    Pid= obj.pid
    print('script executed',Pid)


run()





