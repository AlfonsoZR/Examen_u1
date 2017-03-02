from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
# Create your models here.
class Libro(models.Model):
    nombre  = models.CharField(max_length = 50)
    autor = models.CharField(max_length = 70)
    editorial = models.CharField(max_length = 50)
    ISBN = models.CharField(max_length = 50)
    precio = models.DecimalField(max_digits=19999, decimal_places=2)

    def __unicode__(self):
        return self.nombre
