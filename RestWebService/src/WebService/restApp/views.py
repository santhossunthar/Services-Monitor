from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import HealthCheck
from .serializers import HealthCheckSerializer

# Create your views here.

@api_view(['POST'])
def addServiceLogData(request):
    data = request.data
    print(data)
    return HttpResponse("Hello, World!")

@api_view(['GET'])
def checkHealth(request, service=None):
    if service_name:
        health_check = HealthCheck.objects.filter(application_name=service_name).first()
        if health_check:
            serializer = HealthCheckSerializer(health_check)
            return Response(serializer.data)
        return Response({'message': 'Service not found'}, status=404)
    else:
        health_checks = HealthCheck.objects.all()
        serializer = HealthCheckSerializer(health_checks, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def checkHealthStatus(request):
    return Response()