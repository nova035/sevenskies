from __future__ import unicode_literals
from django.conf.urls import url, patterns
from common.views import (LocationView, LocationDetailView, IndustryView, IndustryDetailView, ContactTypeView,
                          ContactTypeDetailView, ContactView, ContactDetailView)


urlpatterns = patterns(
    '',
    url(r'^locations/$', LocationView.as_view(), name='locations_list'),
    url(r'^locations/(?P<pk>[^/]+)/$', LocationDetailView.as_view(), name='location_detail'),

    url(r'^industries/$', IndustryView.as_view(), name='industries_list'),
    url(r'^industries/(?P<pk>[^/]+)/$', IndustryDetailView.as_view(), name='industry_detail'),

    url(r'^contact_types/$', ContactTypeView.as_view(), name='contact_type_list'),
    url(r'^contact_types/(?P<pk>[^/]+)/$', ContactTypeDetailView.as_view(), name='contact_type_detail'),

    url(r'^contacts/$', ContactView.as_view(), name='contacts_list'),
    url(r'^contacts/(?P<pk>[^/]+)/$', ContactDetailView.as_view(), name='contacts_detail'),
)
