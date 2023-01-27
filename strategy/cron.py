"""import os

import django

from qca_strategy_engine.strategy_settings import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qca_strategy_engine.settings')
django.setup()
from qca_strategy_engine.strategy_settings.models import Strategy_details

obj = Strategy_details.objects.values_list('Initialize_Time','Script')
print(obj)"""

from django_cron import CronJobBase, Schedule,

class MyCronJob(CronJobBase):
    RUN_AT_TIME = ["14:07"]
    #RUN_MONTHLY = ['26']
    ALLOW_PARALLEL_RUNS = True


    schedule = Schedule(run_at_times=RUN_AT_TIME)

    code = 'my_app.my_cron_job'  # a unique code
    print(f'{schedule.run_at_times}')

    def do(self):
        print('Running')