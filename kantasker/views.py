from django.views.generic import TemplateView, CreateView
from kantasker.forms import CrispyUserCreationForm


class HomePageView(TemplateView):
    template_name = 'home_page.html'


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = CrispyUserCreationForm