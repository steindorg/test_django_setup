from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'app_1.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^lists/the-only-list-in-the-world/$', 'app_1.views.view_list',
        name='view_list'
    ),
    #url(r'^admin/', include(admin.site.urls)),
)
