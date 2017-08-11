from django.http import HttpResponse
from django.template import loader
from django.views.generic import View
from .forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

class UserFormView(View):
    form_class = UserForm
    template_name = "datacloud/index.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard/')
        else:
            print("Client GET requested register.html")
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = "datacloud/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('../dashboard/')
        else:
            print("Client GET requested login.html")
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect('../dashboard/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("<h1>Login Failed</h1>")