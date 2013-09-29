from django.views.generic import ListView, DetailView, CreateView
from braces.views import LoginRequiredMixin, SelectRelatedMixin, PrefetchRelatedMixin
from related.views import CreateWithRelatedMixin
from .forms import ProjectCreateForm, CardCreateForm
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


class CardDetailView(DetailView):
    model = Card


class CardCreateView(LoginRequiredMixin, SelectRelatedMixin, CreateWithRelatedMixin, CreateView):
    model = Card
    login_url = "/login/"
    template_name_suffix = '_create'
    select_related = ['board']
    related_model = Project
    form_class = CardCreateForm

    def get_form(self, form_class):
        form = super(CardCreateView,self).get_form(form_class) #instantiate using parent
        form.fields['board'].queryset = Board.objects.filter(project=self.related_object)
        return form
