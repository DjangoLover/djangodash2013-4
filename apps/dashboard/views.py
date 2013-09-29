from braces.views import SelectRelatedMixin, LoginRequiredMixin
from django.views.generic import TemplateView
from apps.projects.models import Project


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):

        context = super(UserDashboardView, self).\
            get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(owner=self.request.user)

        return context

