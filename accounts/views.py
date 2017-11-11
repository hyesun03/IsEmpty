from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class JoinView(TemplateView):
    template_name = 'join.html'

class LoginView(TemplateView):
    template_name = 'login.htmls'