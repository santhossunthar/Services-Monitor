from django.db import models
from elasticsearch_dsl import Document, Text, Keyword

# Create your models here.

class HealthCheck(Document):
    application = Keyword()
    applicationStatus = Keyword()
    host = Text()

    class Index:
        name = 'healthcheck'
