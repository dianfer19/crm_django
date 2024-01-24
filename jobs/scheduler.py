from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

def prueba():
    print('OA')
def start():
    try:
        scheduler = BackgroundScheduler(timezone="America/Guayaquil")
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(func=prueba, trigger="interval", minutes=1,
                          id="prueba1")

        scheduler.print_jobs()
        print("Start Job")
        scheduler.start()
    except Exception as e:
        print("Stopping scheduler..." + str(e))
        scheduler.shutdown()
