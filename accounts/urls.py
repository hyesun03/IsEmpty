from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import Signup, Signup_ok, Ok

app_name = 'accounts'

urlpatterns = [
    url(r'^ok/$', Ok.as_view()),
    url(r'^login/$', auth_views.login, name='login_url'),
    url(r'^logout/$', auth_views.logout, {'next_page' : '/login/'}),
    url(r'^signup/$', Signup.as_view(), name='signup'),
    url(r'^signup_ok/$', Signup_ok.as_view(), name='success_signup')
]