
from django.contrib import admin
from django.urls import path
from jobs import scheduler
urlpatterns = [
    path('admin/', admin.site.urls),
]
scheduler.start()