from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from minimax.views import *
from minimax.utils.translation_utils import set_language_and_region


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/minimax/images/favicon.ico')),
    url(r'^s3direct/', include('s3direct.urls')),

    # dummy urls, until implemented
    url('^people-people-akademie/$', people_akademie, name='people-akademie'),
    url('^people$', home, name='people'),
    url('^people-qualification_and_education', home, name='people-qualification_and_education'),
    url('^people-bma_monteur', home, name='people-bma_monteur'),
    url('^service-reliability', home, name='service-reliability'),

    # slug urls
    url(r'^technologies/(?P<slug_1>[-\w]+)/(?P<slug>[-\w]+)/$', page_details, name='page-details'),
    url(r'^solutions/(?P<slug_1>[-\w]+)/(?P<slug>[-\w]+)/$', page_details, name='page-details'),
    url(r'^(?P<region>[-\w]{2})/(?P<language_code>[-\w]{2})/?$', home, name='home'),
    url('^set_region/(?P<region_code>[-\w]+)/(?P<language_code>[-\w]+)/$', set_language_and_region,
        name='set_language_and_region'),
    url(r'^(?P<region>[-\w]{2})/(?P<language_code>[-\w]{2})/(?P<slug_1>[-\w]+)/(?P<slug_2>[-\w]+)/(?P<slug>[-\w]+)/$', page_details, name='page-details'),
    url(r'^(?P<region>[-\w]{2})/(?P<language_code>[-\w]{2})/(?P<slug_1>[-\w]+)/(?P<slug>[-\w]+)/$', page_details, name='page-details'),
    url(r'^(?P<region>[-\w]{2})/(?P<language_code>[-\w]{2})/(?P<slug>[-\w]+)/$', page_details, name='page-details'),


    url('^$', home, name='home'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

