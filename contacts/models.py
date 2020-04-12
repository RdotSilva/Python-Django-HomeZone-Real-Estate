from django.db import models
from datetime import datetime


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()

