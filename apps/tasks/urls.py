from django.urls import path
from apps.tasks.views import index, task, new_task, edit_task, search, all_tasks  # noqa: E501


app_name = 'tasks'

urlpatterns = [
    path('', index, name='index'),
    path('tasks/<int:id>/', task, name='task'),
    path('all-tasks/', all_tasks, name='all_tasks'),
    path('search/', search, name='search'),
    path('new-task/', new_task, name='new_task'),
    path('edit-task/<int:id>/', edit_task, name='edit_task'),
]
