from django.core.management.base import BaseCommand
from app.models import Entry, Attachment

class Command(BaseCommand):
    help = "Delete ALL entries and attachments"

    def handle(self, *args, **options):
        Attachment.objects.all().delete()
        Entry.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("All entries deleted"))
