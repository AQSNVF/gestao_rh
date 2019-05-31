from django.urls import path
from .views import (
    ColaboradoresList,
    ColaboradorEdit,
    ColaboradorDelete,
    ColaboradorNovo,
    Pdf
)

from.views import rel_HE_colab_reportlab, rel_HE_colab_emp_reportlab

urlpatterns = [
    path('', ColaboradoresList.as_view(), name='list_colaboradores'),
    path('novo/', ColaboradorNovo.as_view(), name='create_colaborador'),
    path('editar/<int:pk>/', ColaboradorEdit.as_view(), name='update_colaborador'),
    path('delete/<int:pk>/', ColaboradorDelete.as_view(), name='delete_colaborador'),
    path('rel-HE-colab-reportlab', rel_HE_colab_reportlab, name='rel_he_colab_reportlab'),
    path('rel-HE-colab-emp-reportlab', rel_HE_colab_emp_reportlab, name='rel_he_colab_emp_reportlab'),
    path('rel-HE-colab-emp-xlwt', Pdf.as_view(), name='rel_he_colab_emp_xlwt'),
]



rel_HE_colab_emp_reportlab