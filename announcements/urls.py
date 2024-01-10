from announcements.views import detail, dismiss
from announcements.views import CreateAnnouncementView, UpdateAnnouncementView
from announcements.views import DeleteAnnouncementView, AnnouncementListView
from django.urls import re_path

urlpatterns = [  # "",
    re_path(r"^$", AnnouncementListView.as_view(), name="announcements_list"),
    re_path(r"^announcement/create/$", CreateAnnouncementView.as_view(), name="announcements_create"),
    re_path(r"^announcement/(?P<pk>\d+)/$", detail, name="announcements_detail"),
    re_path(r"^announcement/(?P<pk>\d+)/hide/$", dismiss, name="announcements_dismiss"),
    re_path(r"^announcement/(?P<pk>\d+)/update/$", UpdateAnnouncementView.as_view(), name="announcements_update"),
    re_path(r"^announcement/(?P<pk>\d+)/delete/$", DeleteAnnouncementView.as_view(), name="announcements_delete"),
]
