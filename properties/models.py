from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    area = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name
    