from django.db import models
from apps.colaboradores.models import Colaborador


class Registrohoraextra(models.Model):
    motivo = models.CharField(max_length=100)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)


    def __str__(self):
        return self.motivo


