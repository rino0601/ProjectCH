# coding=utf-8
# Create your models here.
from django.db import models


class Unit(models.Model):
    sound_file = models.FileField()
    pronounce_text = models.TextField()

    class Meta(object):
        ordering = ['pronounce_text']


class Query(models.Model):
    """
    this represents a request.
    """
    units = models.ManyToManyField(Unit)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        ordering = ['-posted_on']


class Analects(models.Model):
    """
    this represents a result with response.
    """
    query = models.ForeignKey(Query)
    text = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        ordering = ['-posted_on', 'text']