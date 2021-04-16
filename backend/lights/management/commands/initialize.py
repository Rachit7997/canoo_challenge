from django.core.management import BaseCommand
from lights.models import Light
from thermostat.models import Temperature

class Command(BaseCommand):
    def handle(self, *args, **options):
        L1 = Light()
        L1.name = "L1"
        L1.save()
        L2 = Light()
        L2.name = "L2"
        L2.save()

        T = Temperature()
        T.temp = 64
        T.save()