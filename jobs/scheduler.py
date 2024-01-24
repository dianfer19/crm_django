from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

from prueba.models import BandejaElectronica


def prueba():
    query = BandejaElectronica.objects.filter(estado_notificacion="P")
    for item in query:
        print(item)


def start():
    scheduler = BackgroundScheduler(timezone="America/Guayaquil")
    try:
        # scheduler = BackgroundScheduler(timezone="America/Guayaquil")
        scheduler.remove_all_jobs()
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(func=prueba, trigger="interval", seconds=10, id="test")
        scheduler.print_jobs()
        scheduler.start()
    except Exception as e:
        print("Deteniendo los jobs" + str(e))
        # scheduler.shutdown()
