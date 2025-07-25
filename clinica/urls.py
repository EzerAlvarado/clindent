from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('clientes', views.ClienteViewSet)
router.register('aseguranzas', views.AseguranzaViewSet)
router.register('gastos', views.GastoViewSet)
router.register('historial-medico', views.HistorialMedicoViewSet)
router.register('usuarios', views.UsuarioViewSet)
router.register('claims', views.ClaimViewSet)
router.register('grupos', views.GrupoViewSet)

urlpatterns = router.urls