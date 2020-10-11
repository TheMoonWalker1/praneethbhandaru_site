from django.contrib import admin

from .apps.contact.models import ContactInfo
from .apps.projects.models import Project
from .apps.achievements.models import Achievement

admin.site.register(ContactInfo)
admin.site.register(Project)
admin.site.register(Achievement)