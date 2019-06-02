from rest_framework import serializers
from apps.colaboradores.models import Colaborador
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer



class ColaboradorSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)
    class Meta:
        model = Colaborador
        fields = ('id', 'nome', 'user', 'empresa', 'departamentos', 'imagem',
                  'total_horas_extras', 'registrohoraextra_set')


