from rest_framework import viewsets
from apps.colaboradores.api.serializers import ColaboradorSerializer
from apps.colaboradores.models import Colaborador
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

