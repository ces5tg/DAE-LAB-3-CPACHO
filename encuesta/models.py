from django.db import models

class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('datepublished')
class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta , on_delete = models.CASCADE)
    opcion_text =models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
class Prueba(models.Model):
    name= models.CharField(max_length=200)
    

 



















 