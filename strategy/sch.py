from apscheduler.schedulers.background import BackgroundScheduler
from .tests import update

def strat():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update,'interval',seconds = 2)
    scheduler.start()