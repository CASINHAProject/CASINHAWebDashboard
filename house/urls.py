from django.conf.urls import url
from . import views

app_name = 'house'

urlpatterns = [
	#url(r'^$', views.index, name='index'),
	url(r'^add/$', views.add, name='add'),
	url(r'^add/message/$', views.addMessage, name='add'),
	url(r'^detail/(?P<pk>[0-9]+)/$', views.house_detail, name='house_detail'),
]
