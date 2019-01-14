from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.CharField(max_length=10000)

    def __str__(self):
        return self.name + ' - ' + self.quantity


class Asset(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    group = models.CharField(max_length=250)
    size = models.CharField(max_length=250)
    itemSlot = models.CharField(max_length=250)
    estimatedPrice = models.FloatField(max_length=1000)
