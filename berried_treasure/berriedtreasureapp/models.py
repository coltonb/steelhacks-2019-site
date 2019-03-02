from django.db import models

# Create your models here.

class Entry(models.Model):
    name = models.CharField(max_length=12)
    date = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=80)
    