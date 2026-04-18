from django.views.generic import ListView, DetailView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = "seredaApp/task_list.html"
    context_object_name = "seredaApp"

class TaskDetailView(DetailView):
    model = Task
    template_name = "seredaApp/task_detail.html"
    context_object_name = "seredaApp"