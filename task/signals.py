# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from .models import Task
# from .tasks import process_task  # если используешь Celery

"""
Это пример сигналов

По хорошему можно было бы и так реалитзовать
Цеплять состояние объекта и отталкиваясь от этого проводить какие либо махзинации
Например - process_task_service.delay(instance.id) вызвать таску здесь в сигнале
А внутри самой таски уже обрабатывать логику через сервисы и тд тп

"""


# @receiver(post_save, sender=Task)
# def update_task_status(sender, instance, created, **kwargs):
#     if created:
#         process_task_service.delay(instance.id)

# @receiver(pre_save, sender=Task)
# def task_pre_save(sender, instance, created, **kwargs):
#     if created:
#         return
#     if instance.status is None:
#         instance.status = TASK_STATUSES[0][0]  # Установка статуса по умолчанию
#
#     if instance.title:
#         instance.title = instance.title.strip().capitalize()
