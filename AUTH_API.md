# API de Autenticación - Documentación

## Descripción General

Sistema de autenticación completo para la aplicación de clínica, utilizando JWT (JSON Web Tokens) para la autenticación de usuarios.

## Características

- ✅ Login con JWT
- ✅ Logout con invalidación de tokens
- ✅ Perfil de usuario
- ✅ Cambio de contraseña
- ✅ Verificación de autenticación
- ✅ Tokens de acceso y refresh
- ✅ Permisos basados en roles

## Endpoints

### 1. Login
**POST** `/clinica/login/`

Autentica un usuario y devuelve tokens JWT.

**Request:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response (Éxito):**
```json
{
  "success": true,
  "message": "Login exitoso",
  "user": {
    "id": 1,
    "username": "admin",
    "first_name": "Administrador",
    "last_name": "Sistema",
    "email": "admin@clinica.com",
    "clave": null,
    "puede_editar": true,
    "es_admin": true,
    "is_active": true,
    "date_joined": "2024-01-01T00:00:00Z"
  },
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
}
```

**Response (Error):**
```json
{
  "success": false,
  "message": "Error en las credenciales",
  "errors": {
    "non_field_errors": [
      "Credenciales inválidas. Por favor, verifica tu usuario y contraseña."
    ]
  }
}
```

### 2. Logout
**POST** `/clinica/logout/`

Cierra la sesión del usuario e invalida el token de refresh.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request:**
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Logout exitoso"
}
```

### 3. Perfil de Usuario
**GET** `/clinica/profile/`

Obtiene la información del usuario autenticado.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
{
  "success": true,
  "user": {
    "id": 1,
    "username": "admin",
    "first_name": "Administrador",
    "last_name": "Sistema",
    "email": "admin@clinica.com",
    "clave": null,
    "puede_editar": true,
    "es_admin": true,
    "is_active": true,
    "date_joined": "2024-01-01T00:00:00Z"
  }
}
```

**PUT** `/clinica/profile/`

Actualiza la información del usuario autenticado.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request:**
```json
{
  "first_name": "Juan",
  "last_name": "Pérez",
  "email": "juan.perez@clinica.com"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Perfil actualizado exitosamente",
  "user": {
    "id": 1,
    "username": "admin",
    "first_name": "Juan",
    "last_name": "Pérez",
    "email": "juan.perez@clinica.com",
    "clave": null,
    "puede_editar": true,
    "es_admin": true,
    "is_active": true,
    "date_joined": "2024-01-01T00:00:00Z"
  }
}
```

### 4. Cambiar Contraseña
**POST** `/clinica/change-password/`

Cambia la contraseña del usuario autenticado.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request:**
```json
{
  "old_password": "admin123",
  "new_password": "nueva123",
  "confirm_password": "nueva123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Contraseña cambiada exitosamente"
}
```

### 5. Verificar Autenticación
**GET** `/clinica/check-auth/`

Verifica si el usuario está autenticado.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
{
  "success": true,
  "authenticated": true,
  "user": {
    "id": 1,
    "username": "admin",
    "first_name": "Administrador",
    "last_name": "Sistema",
    "email": "admin@clinica.com",
    "clave": null,
    "puede_editar": true,
    "es_admin": true,
    "is_active": true,
    "date_joined": "2024-01-01T00:00:00Z"
  }
}
```

## Configuración de JWT

### Tokens
- **Access Token**: Válido por 1 hora
- **Refresh Token**: Válido por 7 días
- **Rotación automática**: Los refresh tokens se rotan automáticamente
- **Blacklist**: Los tokens usados se invalidan

### Headers de Autorización
Para usar endpoints protegidos, incluye el header:
```
Authorization: Bearer <access_token>
```

## Crear Superusuario

### Comando Personalizado
```bash
python manage.py crear_superusuario
```

### Opciones del Comando
```bash
# Con valores por defecto
python manage.py crear_superusuario

# Con valores personalizados
python manage.py crear_superusuario \
  --username admin \
  --email admin@clinica.com \
  --password admin123 \
  --first-name Administrador \
  --last-name Sistema
```

### Valores por Defecto
- **username**: admin
- **email**: admin@clinica.com
- **password**: admin123
- **first_name**: Administrador
- **last_name**: Sistema

## Ejemplos de Uso

### 1. Login y Uso de API

```bash
# 1. Login
curl -X POST http://localhost:8000/clinica/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'

# 2. Usar el token para acceder a endpoints protegidos
curl -X GET http://localhost:8000/clinica/clientes/ \
  -H "Authorization: Bearer <access_token>"

# 3. Obtener perfil
curl -X GET http://localhost:8000/clinica/profile/ \
  -H "Authorization: Bearer <access_token>"

# 4. Logout
curl -X POST http://localhost:8000/clinica/logout/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "<refresh_token>"
  }'
```

### 2. JavaScript/Frontend

```javascript
// Login
const loginResponse = await fetch('/clinica/login/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    username: 'admin',
    password: 'admin123'
  })
});

const loginData = await loginResponse.json();
const accessToken = loginData.tokens.access;

// Usar token para requests
const response = await fetch('/clinica/clientes/', {
  headers: {
    'Authorization': `Bearer ${accessToken}`
  }
});
```

## Seguridad

### Características de Seguridad
- ✅ Tokens JWT con expiración
- ✅ Invalidación de tokens en logout
- ✅ Validación de contraseñas
- ✅ Protección CSRF
- ✅ Headers de autorización
- ✅ Validación de permisos

### Recomendaciones
1. **Almacenar tokens de forma segura** (localStorage, sessionStorage, cookies httpOnly)
2. **Renovar tokens automáticamente** antes de que expiren
3. **Invalidar tokens en logout** para mayor seguridad
4. **Usar HTTPS en producción**
5. **Validar permisos en el frontend y backend**

## Permisos y Roles

### Campos del Usuario
- `es_admin`: Indica si es administrador del sistema
- `puede_editar`: Indica si puede editar datos
- `is_active`: Indica si la cuenta está activa
- `is_staff`: Indica si tiene acceso al admin de Django
- `is_superuser`: Indica si es superusuario

### Uso de Permisos
```python
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class MiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
``` 