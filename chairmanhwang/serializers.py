# coding=utf-8
from rest_framework import serializers

from chairmanhwang.models import *


__author__ = 'lemonApple'


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ('sound_file', 'pronounce_text', 'id',)


class QuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Query
        fields = ('units', 'result_sound', 'posted_on', 'id',)
        extra_kwargs = {'result_sound': {'required': False}}