from rest_framework import response
from rest_framework.decorators import api_view
import requests

@api_view(['POST'])
def addServiceLogData(request):
    log_data = request.data
    response = requests.post('http://localhost:5601', json=log_data)
    return response