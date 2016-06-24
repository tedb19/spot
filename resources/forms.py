from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.formsets import BaseFormSet

from .models import Resource, ResourceProperty


class ResourceForm(forms.Form):

    ''' Form for registering a new resource for a project '''

    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('Resource Name'), 'class': 'form-control',
               'autofocus': 'true'}))

    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Resource Description'), 'class': 'form-control', 'rows': 2}),
        required=False)

    class Meta:
        model = Resource
        exclude = ('project',)


class ResourcePropertyForm(forms.Form):

    ''' Form for registering a new property for a given resource '''

    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('Property Name'), 'class': 'form-control',
               'autofocus': 'true'}))

    value = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('value'), 'class': 'form-control'}))


def make_form():
    class ResourcePropertyForm(forms.Form):

        ''' Form for registering a new property for a given resource '''

        name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': _('Property Name'), 'class': 'form-control lastrow prop_name',
                   'autofocus': 'true'}))

        value = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': _('value'), 'class': 'form-control prop_value'}))

    return ResourcePropertyForm


class ResourcePropertyFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that there are no duplicate properties
        and that all properties have both a name and a value.
        """
        if any(self.errors):
            return

        names = []
        values = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                name = form.cleaned_data['name']
                value = form.cleaned_data['value']

                # Check that no two links have the same anchor or URL
                if name and value:
                    if name in names:
                        duplicates = True
                    names.append(name)

                if duplicates:
                    raise forms.ValidationError(
                        'Property names must be unique.',
                        code='duplicate_links'
                    )

                # Check that all links have both an anchor and URL
                if value and not name:
                    raise forms.ValidationError(
                        'A property must have a name.',
                        code='missing_anchor'
                    )
                elif name and not value:
                    raise forms.ValidationError(
                        'A property must have a value.',
                        code='missing_URL'
                    )
