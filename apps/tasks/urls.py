from django.urls import path
from apps.tasks.views import index, task, new_task, edit_task

app_name = 'tasks'

urlpatterns = [
    path('', index, name='index'),
    path('tasks/<int:id>/', task, name='task'),
    path('new-task/', new_task, name='new_task'),
    path('edit-task/<int:id>/', edit_task, name='edit_task'),
]
