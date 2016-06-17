from django.db import models


class TimeStampedModel(models.Model):

    '''
    This is a model mixin for models which
    need to be time stamped
    '''
    created = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
