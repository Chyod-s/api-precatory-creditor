from apscheduler.schedulers.background import BackgroundScheduler
from src.api_main.infraestructure.database.engine import get_db
from .task1 import my_task

def job_wrapper():
    db = next(get_db())
    my_task(db)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_wrapper, 'cron', hour=8, minute=30)
    scheduler.start()
    return scheduler

