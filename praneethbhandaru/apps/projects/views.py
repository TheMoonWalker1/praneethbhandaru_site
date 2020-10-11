from django.shortcuts import render, redirect
from .models import Project


def projects_view(request):
    if request.META['HTTP_HOST'] == 'user.tjhsst.edu':
        DOMAIN = '/2023pbhandar'
    else:
        DOMAIN = ''
        
    projects = list(Project.objects.all().order_by('-date'))
    length = len(projects)
    
    projects2 = [projects[x:x+3] for x in range(0, length, 3)]
    
    return render(request, 'projects.html', {'DOMAIN' : DOMAIN, 'projects' : projects2})
