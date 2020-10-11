from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    link_to_project = models.CharField(max_length=150, default=None, null=True)
    description = models.TextField()

    def __str__(self):
        return str(self.title)
