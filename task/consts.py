from django.utils.translation import gettext_lazy as _

TASK_STATUSES = (
    (0, _('Pending')),
    (1, _('In Progress')),
    (2, _('Completed')),
)