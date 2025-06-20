from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда для создания базового пользователя (при необходимости измените поля)
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin2024@mail.ru',
            username='admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('education')
        user.save()
