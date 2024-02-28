from rest_framework import serializers
from .models import DailyTask

class DailyTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = DailyTask
        fields = ['url','id', 'title', 'description', 'complete']