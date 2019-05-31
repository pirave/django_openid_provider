# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 : */

import .views
try:
    from django.conf.urls import url
except ImportError:  # Django < 1.4
    from django.conf.urls.defaults import patterns, url

urlpatterns = [
    url(r'^$', views.openid_server, name='openid-provider-root'),
    url(r'^decide/$', views.openid_decide, name='openid-provider-decide'),
    url(r'^xrds/$', views.openid_xrds, name='openid-provider-xrds'),
    url(r'^(?P<id>.*)/$', views.openid_xrds, {'identity': True}, name='openid-provider-identity'),
]
