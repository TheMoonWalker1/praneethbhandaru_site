from django.db import models


class Achievement(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return str(self.title)
