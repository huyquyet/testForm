from django.db import models
from django.utils import timezone


class Information(models.Model):
    first_name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)
    email = models.EmailField()
    birthday = models.DateTimeField()
    address = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.email