from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from task.models import Task


class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Создаем несколько тестовых задач
        # НО ЛУЧШЕ СДЕЛАТЬ ФАБРИКИ!!
        self.task1 = Task.objects.create(title="Task 1", description="Description 1", status=1)
        self.task2 = Task.objects.create(title="Task 2", description="Description 2", status=1)

    def test_task_list(self):
        """Тестируем GET /tasks/"""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        titles = [task['title'] for task in response.data]
        self.assertIn(self.task1.title, titles)
        self.assertIn(self.task2.title, titles)

    def test_task_create(self):
        """Тестируем POST /tasks/"""
        data = {"title": "Task 3", "description": "Description 3", "status": 1}
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Task.objects.filter(title="Task 3").exists())

    def test_task_retrieve(self):
        """Тестируем GET /tasks/<pk>/"""
        response = self.client.get(f'/api/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task1.title)

    def test_task_status_update(self):
        """Тестируем PATCH /tasks/<pk>/status/"""
        data = {"status": 2}
        response = self.client.patch(f'/api/tasks/{self.task1.id}/status/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.status, 2)

    def test_task_destroy(self):
        """Тестируем DELETE /tasks/<pk>/delete/"""
        response = self.client.delete(f'/api/tasks/{self.task2.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task2.id).exists())
