from celery import Celery

from app import app
from models import User


from mail import send_daily_reminder, send_monthly_reminder, send_export_job_result

celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)
celery.conf.update(
    timezone='Asia/Kolkata',
    enable_utc=False,
)

# tasks
@celery.task()
def daily_reminders():
    with app.app_context():
        users = User.query.all()
        for user in users:
            send_daily_reminder(user.email)
    return "Daily reminders sent successfully."

@celery.task()
def monthly_reminders():
    with app.app_context():
        users = User.query.all()
        for user in users:
            # generate user's previous month data and pass into the function
            send_monthly_reminder(user.email, data=None)
    return "Monthly reminders sent successfully."

@celery.task()
def export_csv():
    with app.app_context():
        users = User.query.all()
        for user in users:
            # generate user's data to export to csv
            send_export_job_result(user.email, data=None)
    return "Export job result sent successfully."

# scheduled tasks
from celery.schedules import crontab
from datetime import timedelta

celery.conf.beat_schedule = {
    'daily_reminders': {
        'task': 'celery_app.daily_reminders',
        'schedule': crontab(hour=12, minute=33),
        # 'schedule': timedelta(seconds=10),
    },
    'monthly_reminders': {
        'task': 'celery_app.monthly_reminders',
        'schedule': crontab(0, 0, day_of_month='1'),
        # 'schedule': timedelta(seconds=3),
    }
}
