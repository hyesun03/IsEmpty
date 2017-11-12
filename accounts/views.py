from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View
from django.core.urlresolvers import reverse
from .models import User
from .form import UserForm
# Create your views here.

class Signup(View):

    def get(self, request):
        userform = UserForm()
        return render(request, 'registration/signup.html', { "form" : userform })
    
    def post(self, request):
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('/signup_ok')
        else:
            print(userform.errors)
            return render(request, 'registration/signup.html', {"form": userform})

class Signup_ok(TemplateView):
    template_name = 'registration/success_signup.html'

class Ok(TemplateView):
    template_name = 'base.html'
