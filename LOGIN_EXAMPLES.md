# Ejemplos de Login - JSONs para Pruebas

## 1. JSON para Login

```json
{
  "username": "admin",
  "password": "admin123"
}
```

## 2. JSON para Login con Usuario Personalizado

```json
{
  "username": "doctor",
  "password": "doctor123"
}
```

## 3. JSON para Actualizar Perfil

```json
{
  "first_name": "Dr. Juan Carlos",
  "last_name": "García López",
  "email": "juan.garcia@clinica.com"
}
```

## 4. JSON para Cambiar Contraseña

```json
{
  "old_password": "admin123",
  "new_password": "nueva123",
  "confirm_password": "nueva123"
}
```

## 5. JSON para Logout

```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## Comandos para Probar

### 1. Crear Superusuario
```bash
python manage.py crear_superusuario
```

### 2. Login
```bash
curl -X POST http://localhost:8000/clinica/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'
```

### 3. Obtener Perfil (con token)
```bash
curl -X GET http://localhost:8000/clinica/profile/ \
  -H "Authorization: Bearer <access_token>"
```

### 4. Actualizar Perfil
```bash
curl -X PUT http://localhost:8000/clinica/profile/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Dr. Juan Carlos",
    "last_name": "García López",
    "email": "juan.garcia@clinica.com"
  }'
```

### 5. Cambiar Contraseña
```bash
curl -X POST http://localhost:8000/clinica/change-password/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "old_password": "admin123",
    "new_password": "nueva123",
    "confirm_password": "nueva123"
  }'
```

### 6. Verificar Autenticación
```bash
curl -X GET http://localhost:8000/clinica/check-auth/ \
  -H "Authorization: Bearer <access_token>"
```

### 7. Logout
```bash
curl -X POST http://localhost:8000/clinica/logout/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "<refresh_token>"
  }'
```

## Flujo Completo de Prueba

1. **Crear superusuario**
2. **Hacer login** y obtener tokens
3. **Usar access token** para acceder a endpoints protegidos
4. **Obtener perfil** del usuario
5. **Actualizar perfil** (opcional)
6. **Cambiar contraseña** (opcional)
7. **Hacer logout** e invalidar tokens

## Notas Importantes

- Reemplaza `<access_token>` y `<refresh_token>` con los tokens reales obtenidos del login
- Los tokens de acceso expiran en 1 hora
- Los tokens de refresh expiran en 7 días
- Siempre incluye el header `Authorization: Bearer <token>` para endpoints protegidos 