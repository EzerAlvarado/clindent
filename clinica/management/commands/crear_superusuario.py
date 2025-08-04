from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from clinica.models import Usuario

class Command(BaseCommand):
    help = 'Crear un superusuario con datos básicos'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, default='admin', help='Nombre de usuario')
        parser.add_argument('--email', type=str, default='admin@clinica.com', help='Email del usuario')
        parser.add_argument('--password', type=str, default='admin123', help='Contraseña del usuario')
        parser.add_argument('--first-name', type=str, default='Administrador', help='Nombre del usuario')
        parser.add_argument('--last-name', type=str, default='Sistema', help='Apellido del usuario')

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']
        first_name = options['first_name']
        last_name = options['last_name']

        # Verificar si el usuario ya existe
        if Usuario.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'El usuario "{username}" ya existe.')
            )
            return

        # Crear el superusuario
        try:
            user = Usuario.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_staff=True,
                is_superuser=True,
                es_admin=True,
                puede_editar=True,
                is_active=True
            )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Superusuario "{username}" creado exitosamente!\n'
                    f'Email: {email}\n'
                    f'Contraseña: {password}'
                )
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error al crear el superusuario: {str(e)}')
            ) 