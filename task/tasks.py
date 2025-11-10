from celery import shared_task

from task.consts import TASK_STATUSES
from task.models import Task
import logging

logger = logging.getLogger(__name__)


@shared_task
def process_task(task_id):

    try:
        task = Task.objects.get(id=task_id)
        logger.info(" Начало обработки задачи ")

        task.status = TASK_STATUSES.COMPLETED  # можно и сигналом post_save
        task.save()
        logger.info("Завершена обработка задачи ")

    except Task.DoesNotExist:
        logger.error(f"Задача с id={task_id} не найдена")
    except Exception as e:
        logger.error(f"Ошибка при обработке задачи {task_id}: {e}")