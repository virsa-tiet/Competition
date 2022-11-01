from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Participant(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    branch= models.CharField(max_length=50)
    phone = models.IntegerField()
    email= models.EmailField(max_length=50)
    subit = models.URLField(max_length=200)
    subit1 = models.FileField()

    def __str__(self):
        return self.name

