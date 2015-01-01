# Create your views here.
from django.views.generic import TemplateView
from rest_framework import viewsets

from chairmanhwang.serializers import *
from models import *


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return super(IndexView, self).get(request, *args, **kwargs)


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class AnalectsViewSet(viewsets.ModelViewSet):
    queryset = Analects.objects.all()
    serializer_class = AnalectsSerializer
