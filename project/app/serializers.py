from rest_framework import serializers
from .models import Category, Subcategory, Entry, Attachment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"

class EntrySerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(
        many=True,
        read_only=True,
        source="attachment_set"
    )
    class Meta:
        model = Entry
        fields = "__all__"
