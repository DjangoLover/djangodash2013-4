from django.views.generic import ListView, DetailView, CreateView
from braces.views import LoginRequiredMixin, SelectRelatedMixin, PrefetchRelatedMixin
from .forms import ProjectCreateForm
from .models import Project


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(SelectRelatedMixin, DetailView):
    model = Project
    select_related = ["board"]


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    login_url = "/login/"
    template_name_suffix = '_create'
    form_class = ProjectCreateForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.owner = self.request.user
        f.save()
        return super(ProjectCreateView, self).form_valid(form)