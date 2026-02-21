from django.core.management.base import BaseCommand
from app.models import Category, Subcategory

class Command(BaseCommand):
    help = "Delete ALL categories and subcategories"

    def handle(self, *args, **options):
        Subcategory.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("All categories and subcategories deleted"))
