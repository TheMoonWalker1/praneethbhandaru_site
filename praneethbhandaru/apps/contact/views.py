from django.shortcuts import render, redirect
from .models import ContactInfo


def contact_view(request):
    if request.META['HTTP_HOST'] == 'user.tjhsst.edu':
        DOMAIN = '/2023pbhandar'
    else:
        DOMAIN = ''
    return render(request, 'contact.html', {'DOMAIN' : DOMAIN, 'contacts' : ContactInfo.objects.all()})
