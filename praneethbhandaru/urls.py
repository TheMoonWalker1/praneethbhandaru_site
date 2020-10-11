"""praneethbhandaru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .apps.home import views as home_views
from .apps.projects import views as projects_views
from .apps.achievements import views as achievements_views
from .apps.contact import views as contact_views
from .apps.about import views as about_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home_view, name='home'),
    path('home', home_views.home_view, name='home'),
    path('about', about_views.about_view, name='about'),
    path('achievements', achievements_views.achievements_view, name='achievements'),
    path('projects', projects_views.projects_view, name='projects'),
    path('contact', contact_views.contact_view, name='contact'),
]
