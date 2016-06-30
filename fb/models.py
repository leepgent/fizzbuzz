from __future__ import unicode_literals

from django.db import models


class Entry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    start = models.DateTimeField(auto_now_add=True)
    stop = models.DateTimeField(null=True)
    source = models.CharField(max_length=5000, null=True)
    bad_source = models.CharField(max_length=5000, null=True)

    def duration(self):
        d = (self.stop - self.start)
        return d.total_seconds()
