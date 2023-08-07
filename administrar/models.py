from django.db import models


class Tarea(models.Model):
    titulo = models.CharField(max_length=256, default="----")
    estado = models.BooleanField(default=0)
