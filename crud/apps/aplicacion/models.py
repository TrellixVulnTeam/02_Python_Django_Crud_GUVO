from django.db import models


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)


class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    estado = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
