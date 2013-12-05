from django.conf.urls import patterns, include, url
from bgm_app import views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bgm_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^template$', views.template, name='template'),
    url(r'^base$', views.templateWithBase, name='base'),
    url(r'^page1$', views.page1, name='page1'),
    url(r'^page2$', views.page2, name='page2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bgm_app/', include('bgm_app.urls')), # ADD THIS NEW TUPLE!
#    url(r'^register/$', views.register, name='register'), 
)
