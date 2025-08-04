# Create your models here.
from .aseguranza import AseguranzaViewSet
from .clientes import ClienteViewSet
from .gastos import GastoViewSet
from .grupos import GrupoViewSet
from .historial_medico import HistorialMedicoViewSet
from .usuarios import UsuarioViewSet
from .claims import ClaimViewSet

# Importar vistas de autenticación
from . import auth