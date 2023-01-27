from rest_framework import serializers
from .models import Strategy_details, Strategy_Parameters, Add_Symbol, Add_Instance


class Strategy_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy_details
        fields = ['Name','Code','Time_Frame','Type','Initialize_Time','Script']

class Strategy_Parameters_serializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy_Parameters
        fields = ['Strategy','Name','Descrption','Variable_Name','Parameter_Type','Parameter_Value']

class Symbol_serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_Symbol
        fields = ['strategy','Exchange','Symbol','is_Monday','is_Tuesday','is_Wednesday','is_Thursday','is_Friday']

class Instance_serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_Instance
        fields = ['Strategy','Exchange','Symbol','is_Monday','is_Tuesday','is_Wednesday','is_Thursday','is_Friday','Initialize_Time','Terminate_Time']