from django.conf.urls import patterns, url
from .views import ProjectListView

urlpatterns = patterns('',
    url(
        regex=r'^list/$',
        view=ProjectListView.as_view(),
        name='project_list'
    )
)