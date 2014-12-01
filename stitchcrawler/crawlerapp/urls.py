#
# created by Ayush
# mapping views and urls

from django.conf.urls import patterns, url

from crawlerapp import views

urlpatterns = patterns('', 
	# /crawlerapp/
	url(r'^$', views.index, name='index'),
	# /crawlerapp/1/
	url(r'^(?P<website_id>\d+)/$', views.detail, name='detail'),
	# /crawlerapp/1/results/
	url(r'^(?P<website_id>\d+)/results/$', views.results, name='results'),
)
