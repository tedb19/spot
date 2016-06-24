from django.db import models
from django.utils.translation import ugettext_lazy as _

from commons.utils import TimeStampedModel
from project.models import Project


class Resource(TimeStampedModel):

    ''' The resource for a particular project '''

    name = models.CharField(db_column='name', max_length=100)
    description = models.TextField(db_column='description', blank=True, default='')
    project = models.ForeignKey(Project, db_column='project_id')

    def __str__(self):
        return _('Project name: {0}').format(self.name)

    class Meta:
        db_table = 'resource'


class ResourceProperty(TimeStampedModel):

    ''' The property assigned to the resource, and it's value '''

    resource = models.ForeignKey(Resource, db_column='resource_id')
    name = models.CharField(db_column='name', max_length=100)
    value = models.TextField(db_column='value')

    class Meta:
        db_table = 'resource_property'
