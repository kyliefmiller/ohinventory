from django.db import models # type: ignore

class OHEntry(models.Model):
    institution = models.CharField(max_length=100)  
    medium = models.CharField(max_length=100)
    access = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    month = models.CharField(max_length=1000, null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    narrator = models.CharField(max_length=100, null=True, blank=True)
    creator = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=1000, null=True, blank=True)
    topic = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=1000000, null=True, blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)
    date_updated = models.CharField(max_length=100, default="April 12, 2026")

