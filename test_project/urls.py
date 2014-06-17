from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'app_1.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	# The captured text (.+) will get passed to the view as an argument.
	# In other words, if we go to the URL /lists/1/, view_list will get a second argument 
	# after the normal request argument, namely the string "1". 
	# If we go to /lists/foo/, we get view_list(request, "foo").
	url(r'^lists/(\d+)/$', 'app_1.views.view_list', name='view_list'),
	url(r'^lists/(\d+)/add_item$', 'app_1.views.add_item', name='add_item'),
    url(r'^lists/new$', 'app_1.views.new_list', name='new_list'),
    
    
    #url(r'^admin/', include(admin.site.urls)),
)
