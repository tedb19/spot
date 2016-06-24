from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Project


class ProjectForm(forms.Form):

    ''' Form for registering a new project '''

    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('Project Name'), 'class': 'form-control',
               'autofocus': 'true'}))

    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Project Description'), 'class': 'form-control'}))

    class Meta:
        model = Project
