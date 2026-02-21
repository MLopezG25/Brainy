from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.category} - {self.name}"

class Entry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Attachment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    path = models.CharField(max_length=255)

    def __str__(self):
        return self.path
