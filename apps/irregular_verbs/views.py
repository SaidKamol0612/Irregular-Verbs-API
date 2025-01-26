from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import IrregularVerb
from .serializers import IrregularVerbSerializer

class IrregularVerbList(ListAPIView):
    queryset = IrregularVerb.objects.all()
    serializer_class = IrregularVerbSerializer
    
class IrregularVerbDetail(RetrieveAPIView):
    queryset = IrregularVerb.objects.all()
    serializer_class = IrregularVerbSerializer
