from django.db import models
from task.consts import TASK_STATUSES


class Task(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Title',
        null=False,
        blank=False,
        help_text='Введите заголовок задачи'
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True,
        help_text='Описание задачи (необязательно)'
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='Status',
        choices=TASK_STATUSES,
        default=1,
        db_index=True,
        help_text='Статус задачи'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At',
        help_text='Время создания задачи'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At',
        help_text='Время последнего обновления задачи'
    )

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-created_at']


# class BasePDate(models.Model):
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name='Created At',
#         help_text='Время создания задачи'
#     )
#     updated_at = models.DateTimeField(
#         auto_now=True,
#         verbose_name='Updated At',
#         help_text='Время последнего обновления задачи'
#     )
#
# class Task(BasePDate):
#     <. . .>


"""
Здесь бы сделал базовую модель с полями created_at и updated_at как показано выше
Но всвязи с ограниченым временем оставил так как есть
Индексы тоже ставить не стал - тк нет необходимости для такой модели
Хотя вот на статус можно поставить - но он будет меняться  достаточно часто, поэтому so-so решение
"""
