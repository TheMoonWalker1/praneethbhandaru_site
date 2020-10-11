from django.shortcuts import render, redirect


def about_view(request):
    if request.META['HTTP_HOST'] == 'user.tjhsst.edu':
        DOMAIN = '/2023pbhandar'
    else:
        DOMAIN = ''
    return render(request, 'about.html', {'DOMAIN' : DOMAIN})
