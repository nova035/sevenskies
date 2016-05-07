from __future__ import unicode_literals
from django.conf.urls import url, patterns
from organizations.views import OrganizationView, OrganizationDetailView, OrganizationContactView, \
    OrganizationContactDetailView


urlpatterns = patterns(
    '',
    url(r'^contacts/$', OrganizationContactView.as_view(), name='organization_contact_list'),
    url(r'^contacts(?P<pk>[^/]+)/$', OrganizationContactDetailView.as_view(), name='organization_contact_detail'),

    url(r'^$', OrganizationView.as_view(), name='organizations_list'),
    url(r'^(?P<pk>[^/]+)/$', OrganizationDetailView.as_view(), name='organization_detail'),
)
