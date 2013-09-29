from django.views.generic import ListView, DetailView, CreateView
from .models import Project


class ProjectListView(ListView):
    model = Project

