from django.conf.urls import patterns, include, url

from django.contrib import admin
from kantasker.views import HomePageView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kantasker.views.home', name='home'),
    # url(r'^kantasker/', include('kantasker.foo.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
