from django.db import models

# Create your models here.


class Winemaker(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Wine(models.Model):
    winemaker = models.ForeignKey(
        Winemaker, on_delete=models.CASCADE, related_name='wines'
    )
    name = models.CharField(max_length=100, default='No Name')
    type = models.CharField(max_length=100, default='No Type')
    grape = models.CharField(max_length=100, default='No Grape')
    country = models.CharField(max_length=100, default='No Country')
    price = models.FloatField(null=True, blank=True, default=None)
    label = models.TextField(null=True)
    link = models.TextField(null=True)

    def __str__(self):
        return self.name