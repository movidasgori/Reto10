from django.db import models

# Create your models here.

class Hero(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

