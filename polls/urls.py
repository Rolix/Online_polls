from django.conf.urls.defaults import *
 
import views
 
urlpatterns = patterns('', 
 	url(r'^list/$', views.polls_list, name='polls_list'),
	url(r'^detail/(?P<id>\d+)/$', views.polls_detail,name='polls_detail'),
   # url(r'^$', 'checks.views.edit_person'),
)
