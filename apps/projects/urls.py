from django.conf.urls import patterns, url
from .views import ProjectListView, ProjectDetailView, ProjectCreateView

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=ProjectListView.as_view(),
        name='project_list'
    ),
    url(
        regex=r'^detail/(?P<slug>[-\w]+)/$',
        view=ProjectDetailView.as_view(),
        name='project_detail'
    ),
    url(
        regex=r'^new/$',
        view=ProjectCreateView.as_view(),
        name='project_create'
    )
)