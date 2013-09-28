from django.views.generic import DetailView
from apps.profiles.models import KantaskerUser


class ProfileDetailView(DetailView):
    model = KantaskerUser
    slug_field = 'username'
    template_name = 'profiles/detail.html'
