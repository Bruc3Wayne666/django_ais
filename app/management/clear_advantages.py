# app/management/commands/clear_advantages.py
from django.core.management.base import BaseCommand
from app.models import Advantage  # Замените 'app' на имя вашего приложения

class Command(BaseCommand):
    help = 'Удаляет все записи из модели Advantage'

    def handle(self, *args, **kwargs):
        Advantage.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Все записи из Advantage были удалены.'))
