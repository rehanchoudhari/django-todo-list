from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DailyTaskSerializers
from .models import DailyTask


class DailyTaskView(viewsets.ModelViewSet):
    serializer_class = DailyTaskSerializers
    queryset = DailyTask.objects.all()
