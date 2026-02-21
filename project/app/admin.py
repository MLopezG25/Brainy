from django.contrib import admin
from .models import Entry, Category, Subcategory, Attachment

admin.site.register(Entry)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Attachment)
