from django.conf.urls import patterns, url
from .views import ProjectListView, ProjectDetailView

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=ProjectListView.as_view(),
        name='project_list'
    ),
    url(
        regex=r'^(?P<slug>[-\w]+)/$',
        view=ProjectDetailView.as_view(),
        name='project_detail'
    )
)