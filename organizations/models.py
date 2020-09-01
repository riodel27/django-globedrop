from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=250, blank=True, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    country = models.CharField(max_length=250, blank=True, default='')
    city = models.CharField(max_length=250, blank=True, default='')

    picture = models.ImageField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: relation with User

    class Meta:
        ordering = ['created_at']
