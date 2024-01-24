
from django.contrib import admin
from django.urls import path

from prueba.views import iniciar_job

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exec/', iniciar_job)
]
