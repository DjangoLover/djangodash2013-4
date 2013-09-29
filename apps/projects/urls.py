from django.conf.urls import patterns, url
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, CardDetailView, CardCreateView

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=ProjectListView.as_view(),
        name='project_list'
    ),
    url(
        regex=r'^view/(?P<slug>[-\w]+)/$',
        view=ProjectDetailView.as_view(),
        name='project_detail'
    ),
    url(
        regex=r'^new/$',
        view=ProjectCreateView.as_view(),
        name='project_create'
    ),
    url(
        regex=r'^card/(?P<slug>[-\w]+)/$',
        view=CardDetailView.as_view(),
        name='card_detail'
    ),
    url(
        regex=r'^view/(?P<slug>[-\w]+)/new_card/$',
        view=CardCreateView.as_view(),
        name='card_create'
    )
)