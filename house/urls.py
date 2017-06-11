from django.conf.urls import url
from . import views

app_name = 'house'

urlpatterns = [
	#url(r'^$', views.index, name='index'),
	url(r'^add/$', views.add, name='add'),
	url(r'^add/message/$', views.addMessage, name='add'),
	url(r'^detail/(?P<pk>[0-9]+)/$', views.house_detail, name='house_detail'),
	url(r'^detail/(?P<pk>[0-9]+)/participants/$', views.house_participants, name='house_participants'),
	url(r'^search_users/$', views.search_users, name='search_users'),
	url(r'^add_user/$', views.add_user, name='add_user'),
	url(r'^remove_user/$', views.remove_user, name='remove_user'),

]
