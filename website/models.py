from django.db import models


class ViewCounter(models.Model):
    """For counting visits to a URL
    """
    url = models.CharField(max_length=300, unique=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} -- {}'.format(self.url, self.views)
