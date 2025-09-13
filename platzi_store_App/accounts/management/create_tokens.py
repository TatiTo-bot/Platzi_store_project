from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Crea tokens de autenticación para todos los usuarios existentes'

    def handle(self, *args, **options):
        users_without_token = User.objects.filter(auth_token__isnull=True)
        
        for user in users_without_token:
            Token.objects.create(user=user)
            self.stdout.write(
                self.style.SUCCESS(
                    f'Token creado para usuario: {user.username}'
                )
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Proceso completado. Se crearon tokens para {users_without_token.count()} usuarios.'
            )
        )