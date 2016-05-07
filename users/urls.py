from __future__ import unicode_literals
from django.conf.urls import url, patterns

from .views import UserList, UserDetailView, MeView


urlpatterns = patterns(
    '',
    url(r'^$', UserList.as_view(), name='users_list'),
    url(r'^me/$', MeView.as_view(), name='me_view'),
    url(r'^(?P<pk>[^/]+)/$', UserDetailView.as_view(), name='user_detail'),
)
