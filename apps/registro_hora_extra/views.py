import json, csv, xlwt

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)


class HoraExtraList(ListView):
    model = RegistroHoraExtra


    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return RegistroHoraExtra.objects.filter(colaborador__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('update_hora_extra_base')

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()
        colaborador = self.request.user.colaborador
        response = json.dumps(
            {'mensagem': 'Requisição Executada',
             'horas':float(colaborador.total_horas_extras)
             }
        )
        return HttpResponse(response, content_type='application/json')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        registro_he = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['id', 'Colaborador','Motivo', 'Horas','Acumulado.'])

        for registro in registro_he:
            writer.writerow(
                [registro.colaborador.id, registro.colaborador, registro.motivo,
                 registro.horas, registro.colaborador.total_horas_extras
                 ])

        return response

class ExportarParaXLS(View):
    def get (self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Relatorio HE excel.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("Banco de Horas")

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['id', 'Colaborador','Motivo', 'Horas','Acumulado.']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = RegistroHoraExtra.objects.filter(utilizada=False)

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.colaborador.id, font_style)
            ws.write(row_num, 1, registro.colaborador.nome, font_style)
            ws.write(row_num, 2, registro.motivo, font_style)
            ws.write(row_num, 3, registro.colaborador.total_horas_extras, font_style)
            ws.write(row_num, 4, registro.horas, font_style)
            row_num += 1

        wb.save(response)
        return response






