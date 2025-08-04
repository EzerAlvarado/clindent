from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import auth

router = DefaultRouter()
router.register('clientes', views.ClienteViewSet)
router.register('aseguranzas', views.AseguranzaViewSet)
router.register('gastos', views.GastoViewSet)
router.register('historial-medico', views.HistorialMedicoViewSet)
router.register('usuarios', views.UsuarioViewSet)
router.register('claims', views.ClaimViewSet)
router.register('grupos', views.GrupoViewSet)

# URLs de autenticación
auth_urlpatterns = [
    path('login/', auth.LoginView.as_view(), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
    path('profile/', auth.UserProfileView.as_view(), name='profile'),
    path('change-password/', auth.ChangePasswordView.as_view(), name='change-password'),
    path('check-auth/', auth.check_auth, name='check-auth'),
]

urlpatterns = router.urls + auth_urlpatterns