# coding=utf-8
# Create your models here.
from django.db import models


class Unit(models.Model):
    sound_file = models.FileField(upload_to='sound')
    pronounce_text = models.TextField()

    class Meta(object):
        ordering = ['pronounce_text']


class Query(models.Model):
    """
    this represents a request.
    """
    units = models.ManyToManyField(Unit)
    result_sound = models.FileField(upload_to='result')
    # todo, units 순서가 입력 순서와 다르게 나오는데, 입력 순서처럼 보이게 하는 방법 혹은 대체할만한 어떤 방법을 찾을 것.
    # todo, 순서가 안지켜지는 이유는 ManyToManyField여서 그렇다, 기본적으로 pk가지고 order_by 하는 모양, 이러면 어떻게 집어넣든....
    # todo, 따라서, 순서를 저장하는 필드가 필요하다. CommaSeparatedIntegerField 를 쓰면 될듯.
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        ordering = ['-posted_on']