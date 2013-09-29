from django.conf.urls import patterns, url
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, CardDetailView, CardCreateView, ProjectUpdateView, BoardCreateView, ProjectCommentView, CardCommentView, CardDeleteView, BoardDeleteView

urlpatterns = patterns('',
    # project urls
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
        regex=r'edit/(?P<slug>[-\w]+)/$',
        view=ProjectUpdateView.as_view(),
        name='project_update'
    ),

    # board urls
    url(
        regex=r'^view/(?P<slug>[-\w]+)/new_board/$',
        view=BoardCreateView.as_view(),
        name='board_create'
    ),
    url(
        regex=r'^view/(?P<project_slug>[-\w]+)/delete_board/(?P<pk>\d+)/$',
        view=BoardDeleteView.as_view(),
        name='board_delete'
    ),

    # card urls
    url(
        regex=r'^view/(?P<project_slug>[-\w]+)/card/(?P<slug>[-\w]+)/$',
        view=CardDetailView.as_view(),
        name='card_detail'
    ),
    url(
        regex=r'^view/(?P<slug>[-\w]+)/new_card/$',
        view=CardCreateView.as_view(),
        name='card_create'
    ),
    url(
        regex=r'^view/(?P<project_slug>[-\w]+)/delete_card/(?P<slug>[-\w]+)/$',
        view=CardDeleteView.as_view(),
        name='card_delete'
    ),


    # project comments view
    url(
        regex=r'^view/(?P<slug>[-\w]+)/comments/$',
        view=ProjectCommentView.as_view(),
        name='project_comment_list'
    ),

    # card comments view
    url(
        regex=r'^view/(?P<project_slug>[-\w]+)/card/(?P<slug>[-\w]+)/comments/$',
        view=CardCommentView.as_view(),
        name='card_comment_list'
    ),
)