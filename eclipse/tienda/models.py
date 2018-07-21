from django.db import models

# Create your models here.
class Prenda(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    tallas = models.CharField(max_length=100, blank=True, null=True)
    precio = models.IntegerField()
    calificacion = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre
        
class Comentario(models.Model):
    receta = models.ForeignKey(Prenda)
    texto = models.TextField(help_text='Deja tu comentario',  verbose_name='Comentario')

    def __unicode__(self):
        return self.texto