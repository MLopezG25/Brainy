import json
from django.core.management.base import BaseCommand
from app.models import Entry

class Command(BaseCommand):
    help = "Import entries from JSON"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **options):
        with open(options["file"], "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            Entry.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Import completed"))
