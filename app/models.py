from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.SET('DELETED AUTHOR'))
    date = models.DateField()

    def __str__(self):
        return self.name


class Image(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=False, upload_to='uploads')

    def __int__(self):
        return self.item
