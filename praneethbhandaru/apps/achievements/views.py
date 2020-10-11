from django.shortcuts import render, redirect
from .models import Achievement


def achievements_view(request):
    if request.META['HTTP_HOST'] == 'user.tjhsst.edu':
        DOMAIN = '/2023pbhandar'
    else:
        DOMAIN = ''
    return render(request, 'achievements.html', {'DOMAIN' : DOMAIN, 'achievements' : Achievement.objects.all().order_by('-date')})
