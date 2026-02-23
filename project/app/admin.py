from django.contrib import admin
from .models import Entry, Category, Subcategory, Attachment


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name",)
    list_filter = ("category",)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "subcategory")
    search_fields = ("title", "description")
    list_filter = ("category", "subcategory")
    inlines = [AttachmentInline]


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("path", "entry")
