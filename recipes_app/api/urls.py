from rest_framework.routers import DefaultRouter
from django.urls import include, path

from recipes_app.api.views import RecipeViewSet


router = DefaultRouter()
router.register(r'recipe', RecipeViewSet, basename='recipe')
urlpatterns = [path('', include(router.urls)),]
