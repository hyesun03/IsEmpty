from django.conf.urls import url

from . import views


app_name = 'booking'
handler404 = views.Custom404View.get_rendered_view()

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^booking/charts/$', views.BookingChartView.as_view(), name='booking_chart'),
    url(r'booking/create/$', views.BookingCreateView.as_view(), name='booking_create'),
    url(r'^booking/(?P<pk>[0-9]+)/delete/$', views.BookingDeleteView.as_view(), name='booking_delete'),
    url(r'^booking/(?P<pk>[0-9]+)/update/$', views.BookingUpdateView.as_view(), name='booking_update'),
]
