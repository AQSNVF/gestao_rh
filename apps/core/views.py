from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.colaboradores.models import Colaborador


#TODO: Utilização do python manage.py shell no terminal Pycharm
# 02:25  seção 4 - aula 16

@login_required()
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)
