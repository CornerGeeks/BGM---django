from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings # for loading media

from dj import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dj$', views.index, name='index'),
    url(r'^dj/add$', views.add, name='index'),
    )
urlpatterns += patterns(
	'django.views.static',
	(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), )