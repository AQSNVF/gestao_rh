from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from apps.colaboradores.api.views import ColaboradorViewSet
from apps.registro_hora_extra.api.views import RegistroHoraExtraViewSet
from rest_framework import routers
from apps.core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/lista_colaboradores', ColaboradorViewSet)
router.register(r'api/banco_horas-extras', RegistroHoraExtraViewSet)

urlpatterns = [
    path('', include('apps.core.urls')),
    path('colaboradores/', include('apps.colaboradores.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('documento/', include('apps.documentos.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


