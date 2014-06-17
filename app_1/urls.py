from django.conf.urls import patterns, url

urlpatterns = patterns('',
   	url(r'^(\d+)/$', 'app_1.views.view_list', name='view_list'),
	url(r'^(\d+)/add_item$', 'app_1.views.add_item', name='add_item'),
    url(r'^new$', 'app_1.views.new_list', name='new_list'),
    
    
    #url(r'^admin/', include(admin.site.urls)),
)
