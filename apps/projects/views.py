from django.views.generic import ListView, DetailView, CreateView, UpdateView
from braces.views import LoginRequiredMixin, SelectRelatedMixin, PrefetchRelatedMixin
from related.views import CreateWithRelatedMixin
from .forms import ProjectCreateForm, CardCreateForm, ProjectUpdateForm, BoardCreateForm
from .models import Project, Card, Board


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(SelectRelatedMixin, DetailView):
    model = Project
    select_related = ["board","card"]


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


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name_suffix = '_edit'


class BoardCreateView(LoginRequiredMixin, CreateWithRelatedMixin, CreateView):
    model = Board
    login_url = "/login/"
    template_name_suffix = '_create'
    related_model = Project
    form_class = BoardCreateForm


class CardDetailView(DetailView):
    model = Card


class CardCreateView(LoginRequiredMixin, CreateWithRelatedMixin, CreateView):
    model = Card
    login_url = "/login/"
    template_name_suffix = '_create'
    related_model = Project
    form_class = CardCreateForm

    def get_form(self, form_class):
        form = super(CardCreateView,self).get_form(form_class)
        form.fields['board'].queryset = Board.objects.filter(project=self.related_object)
        return form
