# tips from Doncho Minkov:
# 1-> (Optional) Move to app to the project directory
# 2-> Create urls.py file
# 3-> Register the app in settings.py
from django.urls import path

from django_introduction_2024.tasks.views import index

urlpatterns = [
    path('', index)
]