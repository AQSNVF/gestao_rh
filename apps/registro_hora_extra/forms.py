from django.forms import ModelForm
from .models import RegistroHoraExtra
from apps.colaboradores.models import Colaborador


class RegistroHoraExtraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['colaborador'].queryset = Colaborador.objects.filter(
            empresa=user.colaborador.empresa
        )

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'colaborador', 'horas', 'utilizada']