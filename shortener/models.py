from django.db import models


class Link(models.Model):
    short_hash = models.CharField(max_length=6)
    destination_url = models.URLField()

    def __str__(self):
        return f'{self.short_hash} -> {self.destination_url}'
