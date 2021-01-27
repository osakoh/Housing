from django.db import models
from datetime import datetime


class Inquiry(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)  # optional
    inquiry_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)  # optional for users who aren't logged in

    def __str__(self):
        return self.name