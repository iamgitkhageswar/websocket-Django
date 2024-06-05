# myapp/views.py
from django.shortcuts import render

from rest_framework import viewsets
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer


# myapp/views.py

def index(request):
    return render(request, 'index.html')

