from django.db import models

# Create your models here.

class Recipe(models.Model):

  PAGE_SIZE = 12

  dish = models.CharField(max_length=100)
  pic = models.CharField(max_length=300)
