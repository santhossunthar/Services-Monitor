from django.shortcuts import render
from rest_framework import views, serializers, response
from .models import LogEntry
from rest_framework.decorators import api_view
import requests

@api_view(['POST'])
def addServiceLogData(request):
    data = request.data
    response = requests.post('http://localhost:5601', json=logs)