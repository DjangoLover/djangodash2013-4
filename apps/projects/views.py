from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, RedirectView, DeleteView
from django.views.generic.edit import FormMixin
from braces.views import LoginRequiredMixin, SelectRelatedMixin, PrefetchRelatedMixin
from related.views import CreateWithRelatedMixin, RelatedObjectMixin
from .forms import ProjectCreateForm, CardCreateForm, ProjectUpdateForm, BoardCreateForm, ProjectCommentCreateForm, CardCommentCreateForm
from .models import Project, Card, Board, ProjectComment, CardComment


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
    redirect_field_name = 'project_detail'
    template_name_suffix = '_create'
    related_model = Project
    form_class = BoardCreateForm
    success_url = '/projects/'


class BoardDeleteView(DeleteView):
    model = Board
    success_url = '/projects/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class CardDetailView(DetailView):
    model = Card


class CardDeleteView(DeleteView):
    model = Card
    success_url = '/projects/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


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


class ProjectCommentView(RelatedObjectMixin, CreateView):
    model = ProjectComment
    related_model = Project
    template_name_suffix = '_list'
    related_object_name = 'project'
    form_class = ProjectCommentCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectCommentView, self).get_context_data(*args, **kwargs)
        context['comments'] = ProjectComment.objects.filter(project=self.related_object)
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.project = self.related_object
        return super(ProjectCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('project_comment_list', args=(self.related_object.slug,))


class CardCommentView(RelatedObjectMixin, CreateView):
    model = CardComment
    related_model = Card
    template_name_suffix = '_list'
    related_object_name = 'card'
    related_slug_field = 'slug'
    related_slug_url_kwarg = 'slug'
    form_class = CardCommentCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super(CardCommentView, self).get_context_data(*args, **kwargs)
        context['comments'] = CardComment.objects.filter(card=self.related_object, project=self.related_object.project)
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.card = self.related_object
        form.instance.project = self.related_object.project
        return super(CardCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('card_comment_list', kwargs={
            'project_slug':self.related_object.project.slug,
            'slug':self.related_object.slug}
        )
