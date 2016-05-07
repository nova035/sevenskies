from __future__ import unicode_literals
from django.conf.urls import url, patterns, include


urlpatterns = patterns(
    '',
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^common/', include('common.urls', namespace='common')),
    url(r'^organizations/', include('organizations.urls', namespace='organization')),
)
