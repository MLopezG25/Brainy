import json
from django.core.management.base import BaseCommand
from app.models import Category, Subcategory

class Command(BaseCommand):
    help = "Load categories and subcategories from JSON"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str)
    def handle(self, *args, **options):
        with open(options["file"], "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            category_name = item["category"]
            subcats = item["subcategories"]

            category, _ = Category.objects.get_or_create(name=category_name)
            for sub in subcats:
                Subcategory.objects.get_or_create(
                    category=category,
                    name=sub
                )
        self.stdout.write(self.style.SUCCESS("Categories loaded successfully"))
