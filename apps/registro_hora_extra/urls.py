from django.urls import path
from .views import (
    HoraExtraList,
    # ColaboradorEdit,
    # ColaboradorDelete,
    # ColaboradorNovo
)


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('editar/<int:pk>/', ColaboradorEdit.as_view(), name='update_colaborador'),
    # path('novo/', ColaboradorNovo.as_view(), name='create_colaborador'),
    # path('delete/<int:pk>/', ColaboradorDelete.as_view(), name='delete_colaborador'),
]



