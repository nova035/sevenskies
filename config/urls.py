from django.conf.urls import patterns, include, url
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from common.views import APIRoot, root_redirect_view

from rest_auth.views import (LoginView, LogoutView, UserDetailsView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView)


rest_auth_patterns = patterns(
    # re-written from rest_auth.urls because of cache validation

    '',
    # URLs that do not require a session or valid token
    url(r'^password/reset/$', cache_page(0)(PasswordResetView.as_view()), name='rest_password_reset'),
    url(r'^password/reset/confirm/$', cache_page(0)(PasswordResetConfirmView.as_view()),
        name='rest_password_reset_confirm'),
    url(r'^login/$', cache_page(0)(LoginView.as_view()), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout/$', cache_page(0)(LogoutView.as_view()), name='rest_logout'),
    url(r'^user/$', cache_page(0)(UserDetailsView.as_view()), name='rest_user_details'),
    url(r'^password/change/$', cache_page(0)(PasswordChangeView.as_view()), name='rest_password_change'),
)


apipatterns = patterns(
    '',
    url(r'^$', login_required(cache_page(60*60)(APIRoot.as_view())), name='root_listing'),
    url(r'^v1/', include('api.urls', namespace='api')),
    url(r'^rest-auth/', include(rest_auth_patterns, namespace='rest_auth')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls',
        namespace='rest_auth_registration'))
)


urlpatterns = patterns(
    '',
    url(r'^$', root_redirect_view, name='root_redirect'),
    url(r'^api/', include(apipatterns, namespace='api')),
    url(r'^accounts/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/token/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)
