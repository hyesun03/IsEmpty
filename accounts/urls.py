from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import Signup, Signup_ok, Profile, Info

app_name = 'accounts'

urlpatterns = [
    url(r'^profile/$', Profile.as_view(), name='profile_url'),
    url(r'^profile/password_change/$', auth_views.password_change,
        {'template_name' : 'registration/password_change_form.html',
        'post_change_redirect' : '/profile/password_change/done'}),
    url(r'^profile/password_change/done/$', auth_views.password_change_done),
    url(r'^profile/info', Info.as_view()),
    url(r'^login/$', auth_views.login, name='login_url'),
    url(r'^logout/$', auth_views.logout, {'next_page' : '/login/'}),
    url(r'^signup/$', Signup.as_view(), name='signup_url'),
    url(r'^signup_ok/$', Signup_ok.as_view(), name='success_signup_url')
]