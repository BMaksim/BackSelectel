from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.CharField(max_length = 100, primary_key = True)
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class Session(models.Model):
    id = models.CharField(max_length = 100, primary_key = True)
    payers = models.TextField()
    oneword = models.TextField()
    aff_pain = models.TextField()
    pigs = models.TextField()