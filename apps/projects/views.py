from django.views.generic import ListView, DetailView, CreateView
from apps.projects.forms import ProjectCreateForm
from .models import Project


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    template_name_suffix = '_create'
    form_class = ProjectCreateForm