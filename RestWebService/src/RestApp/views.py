from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def addServiceLogData(request):
    return Response()

@api_view(['GET'])
def checkHealth(request):
    return Response()

@api_view(['GET'])
def checkHealthStatus(request):
    return Response()