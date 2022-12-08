from django.db import models
from django.db.models import TextField, DateTimeField
from django.utils import timezone


class Link(models.Model):
    source_link = TextField()
    created_data = DateTimeField(default=timezone.now)

    def __str__(self):
        link = str(self.source_link).split('://')[1]
        host = link.split('/')[0]
        return host
