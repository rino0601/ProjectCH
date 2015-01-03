# coding=utf-8
from rest_framework import serializers

from chairmanhwang.models import Unit, Query, Analects


__author__ = 'lemonApple'


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Unit
        fields = ('sound_file', 'pronounce_text', 'id',)


class QuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Query
        fields = ('units', 'posted_on', 'id',)


class AnalectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Analects
        fields = ('query', 'text', 'posted_on', 'id',)