import os
import json
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from app.models import Category, Subcategory, Entry

class Command(BaseCommand):
    help = "Reset database: delete db, migrate, load categories and entries"

    def handle(self, *args, **options):
        db_path = os.path.join(settings.BASE_DIR, "db.sqlite3")

        # Borrar base de datos
        if os.path.exists(db_path):
            os.remove(db_path)
            self.stdout.write(self.style.WARNING("Database deleted"))
        else:
            self.stdout.write(self.style.WARNING("Database not found, skipping delete"))

        # Migraciones
        call_command("makemigrations")
        call_command("migrate")
        self.stdout.write(self.style.SUCCESS("Database migrated"))

        # Cargar categorías
        categories_file = os.path.join(settings.BASE_DIR, "data", "categories.json")
        if os.path.exists(categories_file):
            call_command("load_categories", categories_file)
        else:
            self.stdout.write(self.style.ERROR("categories.json not found"))

        # Cargar entries de prueba (si existe)
        entries_file = os.path.join(settings.BASE_DIR, "data", "entries.json")
        if os.path.exists(entries_file):
            call_command("import_json", entries_file)
        else:
            self.stdout.write(self.style.WARNING("entries.json not found, skipping"))

        self.stdout.write(self.style.SUCCESS("RESET COMPLETED"))
