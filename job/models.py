from django.db import models

# Create your models here.


"""
django model filed 

html 
validation
db size

"""

class Job(models.Model):
    title = models.CharField(max_length=100)