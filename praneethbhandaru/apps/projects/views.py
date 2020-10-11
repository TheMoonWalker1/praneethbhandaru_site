from django.shortcuts import render, redirect
from .models import Project


def projects_view(request):
    if request.META['HTTP_HOST'] == 'user.tjhsst.edu':
        DOMAIN = '/2023pbhandar'
    else:
        DOMAIN = ''
    return render(request, 'projects.html', {'DOMAIN' : DOMAIN, 'projects' : Project.objects.all().order_by('-date')})
