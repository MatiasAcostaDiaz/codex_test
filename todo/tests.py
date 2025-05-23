from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskAPITest(APITestCase):
    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'Test', 'description': 'Testing'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
