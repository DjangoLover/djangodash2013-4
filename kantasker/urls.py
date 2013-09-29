from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.profiles.views import ProfileDetailView
from kantasker.views import HomePageView, SignUpView
from kantasker.forms import CrispyAuthenticationForm

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kantasker.views.home', name='home'),
    # url(r'^kantasker/', include('kantasker.foo.urls')),
    url(
        regex=r'^$',
        view=HomePageView.as_view(),
        name='home'
    ),
    url(
        regex=r'^login/$',
        view='django.contrib.auth.views.login',
        kwargs={'template_name': 'login.html', 'authentication_form': CrispyAuthenticationForm},
        name='login'
    ),
    url(
        regex=r'^signup/$',
        view=SignUpView.as_view(),
        name='signup'
    ),
    url(
        regex=r'^logout/$',
        view='django.contrib.auth.views.logout',
        kwargs={'next_page': '/'},
        name='logout'
    ),
    url(
        regex=r'^admin/',
        view=include(admin.site.urls)
    ),

    url(
        regex=r'^profiles/(?P<slug>\w+)/$',
        view=ProfileDetailView.as_view(),
        name="profile_detail"
    ),
    url(regex=r'^dashboard/',
        view=include('apps.dashboard.urls')),
    url(regex=r'^project/',
        view=include('apps.projects.urls'))
)
