from django.db import models
from elasticsearch_dsl import Document, Text, Keyword

# Create your models here.

class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
