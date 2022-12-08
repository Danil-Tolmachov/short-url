from django.db import models
from django.db.models import TextField, DateTimeField


class Link(models.Model):
    source_link = TextField()
    created_data = DateTimeField()

    def __str__(self):
        link = str(self.source_link).split('://')[1]
        host = link.split('/')[0]
        return host
