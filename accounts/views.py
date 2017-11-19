from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View
from django.core.urlresolvers import reverse
from .models import User
from .form import UserForm, InfoForm
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

class Profile(TemplateView):
    template_name = 'registration/profile.html'

class Info(View):
    def get(self, request):
        infoform = InfoForm()
        return render(request, 'registration/info.html', { "form" : infoform })

    def post(self, request):
        infoform = InfoForm()
        try:
            password = request.POST.get('password')
            print(password)
            if request.user.check_password(password):
                email = request.POST.get('email')
                phone_number = request.POST.get('phone_number')
                request.user.email = email
                request.user.phone_number = phone_number
                request.user.save()
                return render(request, 'registration/info.html', {"form": infoform})
        except Exception:
            pass
        return render(request, 'registration/info.html', {"form": infoform})

        # if infoform.is_valid():
        #     print("info save")
        #     infoform.save()
        #     return render(request, 'registration/info.html', {"form": infoform})
        # else:
        #     print("error")
        #     print(infoform.errors)
        #     return render(request, 'registration/info.html', {"form": infoform})
    #template_name = 'registration/info.html'
