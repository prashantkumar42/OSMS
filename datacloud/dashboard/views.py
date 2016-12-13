from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout

def index(request):
    if request.user.is_authenticated:
        rbatch = request.GET.get('batch')
        template = loader.get_template('dashboard/dashboard.html')
        context = {
            'username': request.user.username,
            'batch': rbatch
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('../login/')

def logout_view(request):
    logout(request)
    return redirect('/')