from django.conf.urls import url

from . import views

app_name = 'booking'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
]