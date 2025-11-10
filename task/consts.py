from django.utils.translation import gettext_lazy as _

TASK_STATUSES = (
    (0, _('Pending')),
    (1, _('In Progress')),
    (2, _('Completed')),
)

"""
Тут бы я хотел реализовать Choises
from model_utils import Choices


TASK_STATUSES = Choices(
        (0, 'PENDING', _('Pending')),
        (1, 'IN_PROGRESS', _('In Progress')),
        (2, 'COMPLETED', _('Completed')),
    )
    
def get_payment_methods_choices():
    return TASK_STATUSES
Тогда в моделях можно будет обращаться так:
Тогда в модельке можно было сделать мульти поле

status = models.PositiveSmallIntegerField(
        verbose_name=_('Status'),
        choices=get_payment_methods_choices,
        db_index=True
    )

"""