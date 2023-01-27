from qca_strategy_engine.strategy_settings.models import Strategy_details
from .test1 import run
import schedule

schedule.every().day.at("10:43").do(run)
