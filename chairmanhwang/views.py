# coding=utf-8
# Create your views here.
from django.conf import settings
from django.core.files import File
from django.shortcuts import redirect

from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from pydub import AudioSegment

from chairmanhwang.serializers import *
from models import *


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if True:
            return redirect('/api/')
        return super(IndexView, self).get(request, *args, **kwargs)


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.sound_file.delete()
        return super(UnitViewSet, self).destroy(request, *args, **kwargs)


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    @detail_route()
    def generate(self, request, *args, **kwargs):
        # get instance
        instance = self.get_object()

        # build sound file.
        result_sound = AudioSegment.empty()
        unit_sounds_path = (a.sound_file.path for a in instance.units.all())
        for path in unit_sounds_path:
            result_sound += AudioSegment.from_wav(path)
        result_filename = '%s.wav' % instance.id

        # save the sound file.
        instance.result_sound.save(result_filename, File(result_sound.export(format='wav')))

        # show as Response.
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.result_sound.delete()
        return super(QueryViewSet, self).destroy(request, *args, **kwargs)