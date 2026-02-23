from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Entry, Category, Subcategory
from .serializers import EntrySerializer, CategorySerializer, SubcategorySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["title", "category"]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]


class StatsView(APIView):
    def get(self, request):
        return Response({
            "categories": Category.objects.count(),
            "subcategories": Subcategory.objects.count(),
            "entries": Entry.objects.count(),
        })
