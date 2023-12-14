from rest_framework import serializers
from .models import HealthCheck

class HealthCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCheck
        fields = ('service_name', 'service_status', 'service_host')