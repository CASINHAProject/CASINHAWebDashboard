from django.conf.urls import url
from api.views import ActuatorsListView, UpdateLocalizationView

helper_patterns = [
	url(r'^$', ActuatorsListView.as_view(), name='atuadores'),
	url(r'^localization/$', UpdateLocalizationView.as_view(), name='localizacao'),
	#url(r'^portfolios/(?P<pk>[0-9]+)$', PortfolioView.as_view(), name='get_portfolio'),
]

urlpatterns = helper_patterns