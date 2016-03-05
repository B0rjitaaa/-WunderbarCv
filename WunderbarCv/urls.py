from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WunderbarCv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cv.views.index', name='index'),
    url(r'^bio/', 'cv.views.bio', name='bio'),
    url(r'^works/', 'cv.views.works', name='works'),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
