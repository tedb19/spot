from django.utils.translation import ugettext_lazy as _
from django.db import models

from commons.utils import TimeStampedModel


class Project(TimeStampedModel):

    ''' The project whose resources are to be tracked '''

    name = models.CharField(db_column='name', max_length=100)
    description = models.TextField(db_column='description',
                                   blank=True, default='')

    def __str__(self):
        return _('Project name: {0}').format(self.name)

    class Meta:
        db_table = 'project'
