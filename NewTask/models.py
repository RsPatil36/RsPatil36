from django.db import models

# Create your models here.
class Data_saving_db(models.Model):
    Name = models.CharField(max_length=64)
    URL = models.URLField(max_length=100)
    Phone_Number = models.CharField(max_length=10)


