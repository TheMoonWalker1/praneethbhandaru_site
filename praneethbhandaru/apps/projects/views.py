from django.shortcuts import render, redirect
from .models import Project


def projects_view(request):
    if request.META['HTTP_HOST'] == 'user.tjhsst.edu':
        DOMAIN = '/2023pbhandar'
    else:
        DOMAIN = ''
        
    projects = list(Project.objects.all().order_by('-date'))
    length = len(projects)

    if request.user_agent.is_mobile:
        projects2 = [projects[x:x+1] for x in range(0, length, 1)]
    else:
        projects2 = [projects[x:x+3] for x in range(0, length, 3)]
        if len(projects2[-1]) < 3:
            for i in range(len(projects2[-1]), 3):
                projects2[-1].append(Project.objects.none())

    
    return render(request, 'projects.html', {'DOMAIN' : DOMAIN, 'projects' : projects2})
