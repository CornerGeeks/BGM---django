from django.conf.urls import patterns, url
from bgm_app import views
from django.conf import settings # for loading media
urlpatterns = patterns('',

        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^meetup/(?P<meetup_id>\d+)$', views.meetup, name='details'),
        #url(r'^(?P<category_name_url>\w+)/join/$', views.join, name='index'),

        )


# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )