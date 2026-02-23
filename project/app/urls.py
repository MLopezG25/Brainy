from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EntryViewSet, CategoryViewSet, SubcategoryViewSet, StatsView

router = DefaultRouter()
router.register("entries", EntryViewSet)
router.register("categories", CategoryViewSet)
router.register("subcategories", SubcategoryViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/stats/", StatsView.as_view()),
]
