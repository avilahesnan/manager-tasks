from django.contrib import admin
from apps.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'term',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('category', 'user',)
    list_per_page = 10
