from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    link_to_project = models.CharField(max_length=150, default=None, null=True)
    description = models.TextField()
    r = models.CharField(max_length=3, default="255")
    g = models.CharField(max_length=3, default="000")
    b = models.CharField(max_length=3, default="000")
    a = models.CharField(max_length=10, default="0.5")

    def __str__(self):
        return str(self.title)
