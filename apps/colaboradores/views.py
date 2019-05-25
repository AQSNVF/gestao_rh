from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Colaborador
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)


class ColaboradoresList(ListView):
    model = Colaborador

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return Colaborador.objects.filter(empresa=empresa_logada)


class ColaboradorEdit(UpdateView):
    model = Colaborador
    fields = ['nome', 'departamentos']


class ColaboradorDelete(DeleteView):
    model = Colaborador
    success_url = reverse_lazy('list_colaboradores')


class ColaboradorNovo(CreateView):
    model = Colaborador
    fields = ['nome', 'departamentos']


    def form_valid(self, form):
        colaborador = form.save(commit=False)
        username = colaborador.nome.split(' ')[0] + colaborador.nome.split(' ')[1]
        colaborador.empresa = self.request.user.colaborador.empresa
        colaborador.user = User.objects.create(username=username)
        colaborador.save()
        return super(ColaboradorNovo, self).form_valid(form)