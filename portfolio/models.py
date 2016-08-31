from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify


class PortfolioEntry(models.Model):
    title = models.CharField(max_length=50)
    when_created = models.DateTimeField()
    verbose_title = models.CharField(max_length=200, blank=True)
    verbose_date = models.CharField(max_length=50, blank=True)
    head = models.TextField()
    body = models.TextField()
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.verbose_title:
            self.verbose_title = self.title
        self.slug = slugify(self.title)
        super(PortfolioEntry, self).save(*args, **kwargs)
