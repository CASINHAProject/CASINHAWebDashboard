from django.conf.urls import url
from api.views import ActuatorsListView

helper_patterns = [
	url(r'^$', ActuatorsListView.as_view(), name='atuadores'),
	#url(r'^portfolios/(?P<pk>[0-9]+)$', PortfolioView.as_view(), name='get_portfolio'),
]

urlpatterns = helper_patterns