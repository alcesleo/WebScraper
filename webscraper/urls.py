from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'locallyproduced.views.show', name='show'),
    url(r'^scrape$', 'locallyproduced.views.scrape', name='scrape'),
    url(r'^admin/', include(admin.site.urls)),
)
