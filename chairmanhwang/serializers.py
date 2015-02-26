# coding=utf-8
from rest_framework import serializers

import models

__author__ = 'lemonApple'


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Unit
        fields = ('sound_file', 'pronounce_text', 'id',)


class QuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Query
        fields = ('units', 'result_sound', 'posted_on', 'id',)
        extra_kwargs = {'result_sound': {'required': False}}