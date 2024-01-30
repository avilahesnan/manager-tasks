from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from apps.tasks.models import Task
from apps.tasks.forms import TaskForm


def index(request):
    # if not request.user.is_authenticated:
    #     messages.error(request, 'No users are logged in!')
    #     return redirect('tasks:login')
    
    current_date = timezone.now()
    tasks = Task.objects.filter(term__lt=current_date + timezone.timedelta(days=7)).order_by('term')
    return render(request, 'tasks/index.html', {'tasks': tasks})


def task(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasks/task_view.html', {'is_detail_page': True, 'task': task})


def new_task(request):
    # if not request.user.is_authenticated:
    #     messages.error(request, 'No users are logged in!')
    #     return redirect('tasks:login')
    
    form = TaskForm
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task registered successfully!')
            return redirect('tasks:index')

    return render(request, 'tasks/new_task.html', {"form": form})


def edit_task(request, id):
    # if not request.user.is_authenticated:
    #     messages.error(request, 'No users are logged in!')
    #     return redirect('tasks:login')
    
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task edited successfully!')
            return redirect('tasks:index')

    return render(request, 'tasks/edit_task.html', {"form": form, "id": id})
