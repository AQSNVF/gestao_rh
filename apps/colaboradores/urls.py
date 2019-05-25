from django.urls import path
from .views import (
    ColaboradoresList,
    ColaboradorEdit,
    ColaboradorDelete,
    ColaboradorNovo
)


urlpatterns = [
    path('', ColaboradoresList.as_view(), name='list_colaboradores'),
    path('novo/', ColaboradorNovo.as_view(), name='create_colaborador'),
    path('editar/<int:pk>/', ColaboradorEdit.as_view(), name='update_colaborador'),
    path('delete/<int:pk>/', ColaboradorDelete.as_view(), name='delete_colaborador'),
]



