from unittest.mock import patch

from django.test import TestCase
from task.models import Task, TASK_STATUSES
from task.tasks import process_task

class ProcessTaskTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            status=TASK_STATUSES.PENDING
        )

    def test_process_task_marks_completed(self):
        process_task(self.task.id)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, TASK_STATUSES.COMPLETED)

    def test_process_task_invalid_id(self):
        try:
            process_task(9999)  # несуществующий ID
        except Exception:
            self.fail("process_task поднял исключение при несуществующем ID")

    @patch('api.v1.task.views.process_task.delay')
    def test_task_creation_triggers_celery_task(self, mock_delay):
        data = {
            "title": "Signal Test Task",
            "description": "Test",
            "status": 0  # PENDING
        }
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, 201)

        task = Task.objects.get(title="Signal Test Task")
        mock_delay.assert_called_once_with(task.id)
