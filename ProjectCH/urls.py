# coding=utf-8
from django.conf import settings
from django.conf.urls import patterns, url, include
from rest_framework import routers

from chairmanhwang import views
from chairmanhwang import admin


router = routers.DefaultRouter()
router.register(r'unit', views.UnitViewSet)
router.register(r'query', views.QueryViewSet)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ProjectCH.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.admin_site.urls)),
                       url(r'^$', views.IndexView.as_view()),
                       url(r'^api/', include(router.urls)),
                       url(r'^docs/', include('rest_framework_swagger.urls')), )

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^%s/(?P<path>.*)$' % settings.MEDIA_KEY, 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }),
                            url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.STATIC_ROOT,
                            }), )
