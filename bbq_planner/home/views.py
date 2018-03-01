from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to="/user/dashboard/")
    else:
        template = loader.get_template('home/index.html')
        context = {
            'title': 'Welcome to Send Cloud BBQ Planner'
        }
        return HttpResponse(template.render(context, request))