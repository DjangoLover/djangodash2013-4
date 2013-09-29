from django.conf.urls import patterns, url
from apps.dashboard.views import UserDashboardView


urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=UserDashboardView.as_view(),
        name='dashboard_home'
    )
)