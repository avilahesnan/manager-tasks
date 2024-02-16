from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from apps.tasks.models import Task
from apps.tasks.forms import TaskForm


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'No users are logged in!')
        return redirect('users:login')

    user = request.user
    current_date = timezone.now()
    tasks = Task.objects.filter(  # pylint: disable=no-member
        term__lt=current_date + timezone.timedelta(days=7),
        user=user, is_completed=False).order_by('term')
    return render(request, 'tasks/index.html', {'tasks': tasks})


def task(request, id):  # pylint: disable=redefined-builtin
    task = get_object_or_404(Task, id=id)  # pylint: disable=redefined-outer-name # noqa: E501
    return render(request, 'tasks/task_view.html', {'is_detail_page': True, 'task': task})  # pylint: disable=line-too-long # noqa: E501


def all_tasks(request):
    if not request.user.is_authenticated:
        messages.error(request, 'No users are logged in!')
        return redirect('users:login')

    user = request.user
    tasks = Task.objects.filter(user=user).order_by('term')  # pylint: disable=no-member # noqa: E501
    return render(request, 'tasks/index.html', {'tasks': tasks})


def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'No users are logged in!')
        return redirect('users:login')

    user = request.user
    tasks = Task.objects.filter(user=user).order_by('term')  # pylint: disable=no-member, # noqa: E501
    if 'search' in request.GET:
        name_search = request.GET['search']
        if name_search:
            tasks = tasks.filter(name__icontains=name_search)

    return render(request, 'tasks/index.html', {'tasks': tasks})


def new_task(request):
    if not request.user.is_authenticated:
        messages.error(request, 'No users are logged in!')
        return redirect('users:login')

    user = request.user
    if request.method == 'POST':
        form = TaskForm(request.POST, user=user)
        if form.is_valid():
            task = form.save(commit=False)  # pylint: disable=redefined-outer-name # noqa: E501
            task.user = user
            task.save()
            messages.success(request, 'Task registered successfully!')
            return redirect('tasks:index')
    else:
        form = TaskForm(user=user)

    return render(request, 'tasks/new_task.html', {'form': form})


def edit_task(request, id):  # pylint: disable=redefined-builtin
    if not request.user.is_authenticated:
        messages.error(request, 'No users are logged in!')
        return redirect('users:login')

    user = request.user
    try:
        task = Task.objects.get(id=id, user=user)  # pylint: disable=redefined-outer-name,disable=no-member # noqa: E501
    except Task.DoesNotExist:  # pylint: disable=no-member # noqa: E501
        messages.error(request, 'Task not found or you do not have permission to edit it.')   # pylint: disable=line-too-long # noqa: E501
        return redirect('tasks:index')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, user=user, edit_mode=True)
        if form.is_valid():
            edited_task = form.save(commit=False)
            edited_task.user = user
            edited_task.save()

            messages.success(request, 'Task edited successfully!')
            return redirect('tasks:index')
    else:
        form = TaskForm(instance=task, user=user, edit_mode=True)

    return render(request, 'tasks/edit_task.html', {'form': form, 'id': id})
