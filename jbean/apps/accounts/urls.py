# coding=utf-8
from django.conf.urls import url, patterns
from jbean.apps.accounts.views import AccountProfileView


urlpatterns = patterns(
    '',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password_change/done/$',
        'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$',
        'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(
        r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-['
        r'0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),
    url(r'^profile/$', AccountProfileView.as_view(), name='account_profile'),
    )
