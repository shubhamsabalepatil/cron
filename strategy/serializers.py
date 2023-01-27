from rest_framework import serializers
from .models import Instance_status2

class Instance_status2_serializer(serializers.ModelSerializer):
    class Meta:
        model =Instance_status2
        fields = ['Pids','Pid_status','start_datetime','stop_datetime']