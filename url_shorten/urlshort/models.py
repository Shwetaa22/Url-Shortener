from django.db import models

# Create your models here.
import os
from django.contrib.humanize.templatetags.humanize import naturalday
from django.core.validators import RegexValidator
from django.utils import timezone


class ShortUrl(models.Model):
    original_url = models.TextField()
    short_url = models.TextField()
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=naturalday(timezone.now))
    updated_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(default=naturalday(timezone.now))
    deleted_at = models.DateTimeField(blank=True,null=True)
    is_liked = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'short_url'  # define your custom name

    def save(self, *args, **kwargs):
        super(ShortUrl, self).save(*args, **kwargs)
        return self

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()


