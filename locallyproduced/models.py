from django.db import models

# Create your models here.
class Producer(models.Model):
    """A scraped producer"""
    producer_id = models.IntegerField()
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
