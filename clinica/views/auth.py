"""Vistas para autenticación."""

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from clinica.serializers.auth import (
    LoginSerializer,
    UsuarioSerializer,
    ChangePasswordSerializer
)
from clinica.models import Usuario

class LoginView(APIView):
    """Vista para login de usuarios."""
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        """Realizar login de usuario."""
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # Generar tokens JWT
            refresh = RefreshToken.for_user(user)
            
            # Realizar login de sesión (opcional)
            login(request, user)
            
            return Response({
                'success': True,
                'message': 'Login exitoso',
                'user': UsuarioSerializer(user).data,
                'tokens': {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }
            }, status=status.HTTP_200_OK)
        
        return Response({
            'success': False,
            'message': 'Error en las credenciales',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    """Vista para logout de usuarios."""
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        """Realizar logout de usuario."""
        try:
            # Invalidar token de refresh
            refresh_token = request.data.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            
            # Logout de sesión
            logout(request)
            
            return Response({
                'success': True,
                'message': 'Logout exitoso'
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Error en logout',
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    """Vista para obtener y actualizar perfil de usuario."""
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """Obtener información del usuario actual."""
        serializer = UsuarioSerializer(request.user)
        return Response({
            'success': True,
            'user': serializer.data
        }, status=status.HTTP_200_OK)
    
    def put(self, request):
        """Actualizar información del usuario actual."""
        serializer = UsuarioSerializer(
            request.user, 
            data=request.data, 
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Perfil actualizado exitosamente',
                'user': serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            'success': False,
            'message': 'Error al actualizar perfil',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    """Vista para cambiar contraseña."""
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        """Cambiar contraseña del usuario actual."""
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            
            return Response({
                'success': True,
                'message': 'Contraseña cambiada exitosamente'
            }, status=status.HTTP_200_OK)
        
        return Response({
            'success': False,
            'message': 'Error al cambiar contraseña',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_auth(request):
    """Verificar si el usuario está autenticado."""
    return Response({
        'success': True,
        'authenticated': True,
        'user': UsuarioSerializer(request.user).data
    }, status=status.HTTP_200_OK) 