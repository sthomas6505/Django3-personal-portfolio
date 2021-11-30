from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    details = models.TextField()
    url = models.URLField(blank=True)
