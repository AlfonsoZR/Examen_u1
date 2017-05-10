from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from django.urls import reverse

# Create your models here.
class Libro(models.Model):
    nombre  = models.CharField(max_length = 50)
    autor = models.CharField(max_length = 70)
    editorial = models.CharField(max_length = 50)
    ISBN = models.CharField(max_length = 50)
    precio = models.DecimalField(max_digits=19999, decimal_places=2)
    slug = models.SlugField(blank=True)
    tipo = models.CharField(max_length = 40, blank=True, null = True, default = "Libro" )


    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        print "URL completo"
        mirar_nombre = "libros:detalle_slug"
        return reverse(mirar_nombre, args=[str(self.slug)])

def Libro_pre_save_reciever(sender, instance, *args, **kwargs):
    print sender
    print instance

    if not instance.slug:
        instance.slug = slugify(instance.nombre)

pre_save.connect(Libro_pre_save_reciever, sender=Libro)
