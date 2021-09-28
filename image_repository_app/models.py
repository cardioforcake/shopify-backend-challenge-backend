from django.db import models
from datetime import date



class Image(models.Model):
  title=models.CharField(max_length=200, default='Unkown')
  creator=models.CharField(max_length=200, default='Unkown')
  uploaded=models.DateField(default=date.today)
  url = models.CharField(max_length=200, default='Unknown')

  def __str__(self):
    return f'Image for picture#: {self.id}'

class User(models.Model):
  uid=models.CharField(max_length=200, default='Unknown')
  images=models.ManyToManyField(Image)

  def __str__(self):
    return f'User {self.id}'