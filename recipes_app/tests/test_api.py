from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from recipes_app.models import Recipe
 

class RecipeAPITestCaseHappy(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.recipe_data = {
            "title": "Title test 2",
            "description": "Description test 2",
            "author": self.user.id
        }

    def test_get_recipe(self):
        url = reverse('recipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_recipe(self):
        url = reverse('recipe-list')
        response = self.client.post(url, self.recipe_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_recipe_detail(self):
        recipe = Recipe.objects.create(
        title="Test",
        description="Test desc",
        author=self.user
        )
        url = reverse('recipe-detail', kwargs={'pk': recipe.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RecipeAPITestCaseUnhappy(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.recipe_data = {
            "title": "Title test 2",
            "description": "Description test 2",
            "author": self.user.id
        }

    def test_get_recipe(self):
        url = reverse('recipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_recipe(self):
        url = reverse('recipe-list')
        response = self.client.post(url, self.recipe_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_recipe_detail(self):
        recipe = Recipe.objects.create(
        title="Test",
        description="Test desc",
        author=self.user
        )
        url = reverse('recipe-detail', kwargs={'pk': recipe.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)