from django.contrib import admin
from django_introduction_2024.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'description')
    list_filter = ('id',)
