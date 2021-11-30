from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    details = models.TextField()

    def __str__(self):      # Showss the title in the admin pages.
        return self.title
