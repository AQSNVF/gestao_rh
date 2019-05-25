from django.db import models
from apps.colaboradores.models import Colaborador


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.motivo


