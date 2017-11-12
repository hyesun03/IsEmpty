from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class Signup(FormView):
    def get(self, request, *args, **kwargs):
        userform = UserCreationForm()
        return render(request, 'registration/signup.html', { "userform" : userform })
    def post(self, request, *args, **kwargs):
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return reverse("success_signup")
class Signup_ok(TemplateView):
    template_name = 'registration/success_signup.html'

class Ok(TemplateView):
    template_name = 'base.html'
