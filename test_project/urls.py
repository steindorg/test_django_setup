from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'app_1.views.home_page', name='home'),
	url(r'^lists/', include('app_1.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
