from django.db import models
from django.shortcuts import reverse
from apps.colaboradores.models import Colaborador


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    proprietario = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('update_colaborador', args=[self.proprietario.id])


    def __str__(self):
        return self.descricao



