from django.shortcuts import render

from jobs import scheduler


# Create your views here.
def iniciar_job(request):
    scheduler.start()
    return render(request, "test.html")