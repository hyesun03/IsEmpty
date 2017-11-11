from django.conf.urls import url

from .views import LoginView, JoinView

app_name = 'accounts'

urlpatterns = [
    url(r'^login/', LoginView.as_view()),
    url(r'^join/', JoinView.as_view())
]