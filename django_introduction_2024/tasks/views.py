from django.http import HttpResponse
from django.shortcuts import render
from django import http

from django_introduction_2024.tasks.models import Task


# def index(request):
#     return http.HttpResponse(
#         'Watchlist',
#         # headers={'Content-Type': 'text/plain'},
#
#     )

# def index(request):
#     title_filter = request.GET.get('filter', None)
#     tasks = Task.objects.all()
#
#     if title_filter:
#         tasks = tasks.filter(title__contains=filter)
#     if not tasks:
#         return HttpResponse('<h1>No tasks found!</h1>')
#
#     result = []
#
#     for task in tasks:
#         result.append(f"""
# <li>
#     <h2>{task.title}</h2>
#     <p>{task.description}</p>
# </li>
#         """)
#
#     ul = f"<ul>{''.join(result)}</ul>"
#
#     content = f"""
#     <h1>{len(tasks)} Tasks</h1>
#     {ul}
#     """
#
#     # return http.HttpResponse(content)


def index(request):
    title_filter = request.GET.get('filter', None)
    tasks = Task.objects.all()

    if title_filter:
        tasks = tasks.filter(title__contains=title_filter.lower())
    context = {
        'title': 'Index',
        'tasks': tasks,
        'tasks_count': len(tasks)

    }

    return render(request,'tasks/index.html', context)

