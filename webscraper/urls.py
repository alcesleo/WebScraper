from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'locallyproduced.views.show'),
    url(r'^scrape/', 'locallyproduced.views.scrape'),
    url(r'^admin/', include(admin.site.urls)),
)
