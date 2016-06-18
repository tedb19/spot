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


class ResourceProperty(TimeStampedModel):

    ''' The property assigned to the resource '''
    name = models.CharField(db_column='name', max_length=100)
    description = models.TextField(db_column='description', blank=True, default='')
    data_type = models.CharField(db_column='data_type', max_length=100)

    class Meta:
        db_table = 'resource_property'


class ResourcePropertyValue(TimeStampedModel):

    ''' The value to the property assigned to a resource '''

    resource = models.ForeignKey(Resource, db_column='resource_id')
    resource_property = models.ForeignKey(ResourceProperty, db_column='resource_property_id')
    value = models.TextField(db_column='value')

    class Meta:
        db_table = 'resource_property_value'
