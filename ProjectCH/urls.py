from django.conf.urls import patterns, url, include
# from django.contrib import admin

from chairmanhwang import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'unit', views.UnitViewSet)
router.register(r'query', views.QueryViewSet)
router.register(r'analects', views.AnalectsViewSet)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ProjectCH.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.IndexView.as_view()),
                       url(r'^', include(router.urls)),
)
