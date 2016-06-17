from django.db import models
from django.utils.translation import ugettext_lazy as _

from commons.utils import TimeStampedModel
from project.models import Project


class Resource(TimeStampedModel):

    ''' The resource for a particular project '''

    DEVELOPMENT = 1
    TEST = 2
    STAGING = 3
    PRODUCTION = 4

    ENVIRONMENT_CHOICES = (
        (DEVELOPMENT, _('Development')),
        (TEST, _('Test')),
        (STAGING, _('Staging')),
        (PRODUCTION, _('Production')),
    )

    name = models.CharField(db_column='name', max_length=100)
    description = models.TextField(db_column='description', blank=True, default='')
    project = models.ForeignKey(Project, db_column='project_id')
    environment = models.SmallIntegerField(db_column='environment_id',
                                           choices=ENVIRONMENT_CHOICES,
                                           default=PRODUCTION)

    def __str__(self):
        return _('Project name: {0}').format(self.name)

    class Meta:
        db_table = 'resource'


class Hardware(Resource):

    ''' The hardware resources assigned to the project '''

    serial_number = models.CharField(db_column='serial_number', max_length=100)
    current_location = models.CharField(db_column='current_location', max_length=100)


class System(Resource):

    ''' The sub-system resources that form part of the project '''

    user_name = models.CharField(db_column='user_name', max_length=100)
    password = models.CharField(db_column='password', max_length=100)
    url = models.CharField(db_column='url', max_length=500)


class Documentation(Resource):

    ''' The documentation resources that describe the scope of the project '''

    url = models.CharField(db_column='url', max_length=500)
