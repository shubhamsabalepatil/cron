from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from .serializers import Strategy_details_serializer, Strategy_Parameters_serializer, Symbol_serializer, Instance_serializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .models import Strategy_details




# Create your views here.

def Settings(r):
    return render(r,'home.html')

def login(r):
    return render(r,'login.html')

@api_view(['POST'])
def add_strategy(r):
    try:
        serializer = Strategy_details_serializer(data=r.data)
        if serializer.is_valid():
            serializer.save()
            return Response(('New Strategy Created'), status=status.HTTP_201_CREATED)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    except:
        response = Response(("Invalid Details-Cant Create strategy"), status=status.HTTP_400_BAD_REQUEST)
        return response

@api_view(['GET'])
def view_strategy(r):
    getstrategy = Strategy_details.objects.all()
    serializer = Strategy_details_serializer(getstrategy,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_Parameters(r):
    try:
        serializer = Strategy_Parameters_serializer(data=r.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'New Parameters Created'}, status=status.HTTP_201_CREATED)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    except:
        response = JsonResponse({'msg': "Invalid Details-Cant Create Parameters"}, status=status.HTTP_400_BAD_REQUEST)
        return response


@api_view(['POST'])
def add_Symbol(r):
    try:
        serializer = Symbol_serializer(data=r.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'New Symbol Created'}, status=status.HTTP_201_CREATED)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    except:
        response = JsonResponse({'msg': "Invalid Details-Cant Create Symbol"}, status=status.HTTP_400_BAD_REQUEST)
        return response


@api_view(['POST'])
def add_Instance(r):
    try:
        serializer = Instance_serializer(data=r.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'New Instance Created'}, status=status.HTTP_201_CREATED)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    except:
        response = JsonResponse({'msg': "Invalid Details-Cant Create Instance"}, status=status.HTTP_400_BAD_REQUEST)
        return response







