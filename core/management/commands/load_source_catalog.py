import csv
from django.core.management.base import BaseCommand
from core.models import SourceCatalog

class Command(BaseCommand):
    help = 'Loads source catalog from CSV'

    def handle(self, *args, **kwargs):
        path = 'core/data/source_catalog.csv'
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                SourceCatalog.objects.get_or_create(
                    source_system=row['source_system'],
                    source_field=row['source_field'],
                    description=row['description']
                )
        self.stdout.write(self.style.SUCCESS('Source catalog loaded successfully!'))
