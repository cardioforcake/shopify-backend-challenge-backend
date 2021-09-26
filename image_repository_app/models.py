from django.db import models
from datetime import date

class Image(models.Model):
  title=models.CharField(max_length=200)
  creator=models.CharField(max_length=200, default='unkown')
  created_on=models.DateField(default=date.today)
  url = models.CharField(max_length=200)

  def __str__(self):
    return f"Image for picture#: {self.id}"