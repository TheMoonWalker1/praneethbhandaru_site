from django.db import models


class ContactInfo(models.Model):
    title = models.CharField(max_length=50)
    link_to_contact = models.CharField(max_length=150, default=None)
    description = models.TextField()

    def __str__(self):
        return str(self.title)
