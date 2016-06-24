from django.shortcuts import render, get_object_or_404, redirect
from django.forms.formsets import formset_factory
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.http import JsonResponse
from django.db import IntegrityError, transaction

from user_account.views import LoginRequest
from project.models import Project
from project.views import projects_listing, project_profile

from .forms import ResourcePropertyFormSet, ResourcePropertyForm, ResourceForm, make_form
from .models import ResourceProperty, Resource


def create_resource(request, project_id):
    if not request.user.is_authenticated:
        return redirect(LoginRequest)
    page_title = 'Add Resource'
    template_name = 'resources/create_resource.html'
    project = get_object_or_404(Project, pk=project_id)

    # Create the formset, specifying the form and formset we want to use.
    formset_cls = formset_factory(make_form(), max_num=100)

    if request.method == 'POST':
        if request.POST.get('cancel', None):
            return redirect(project_profile, project.pk)
        resource_form = ResourceForm(request.POST)
        formset = formset_cls(request.POST)

        if resource_form.is_valid() and formset.is_valid():
            if not formset.forms[0].has_changed():
                messages.warning(request,
                                 ("Ooops! Atleast one property is required."))
                return render(request, template_name, locals())

            resource = Resource.objects.create(
                name=resource_form.cleaned_data.get('name'),
                description=resource_form.cleaned_data.get('description'),
                project=project
            )

            properties = []

            for resource_property_form in formset:
                if resource_property_form.has_changed():
                    name = resource_property_form.cleaned_data.get('name')
                    value = resource_property_form.cleaned_data.get('value')

                    if name and value:
                        resource_property = ResourceProperty(resource=resource, name=name, value=value)
                        properties.append(resource_property)

            try:
                with transaction.atomic():
                    ResourceProperty.objects.bulk_create(properties)
                    messages.info(request, 'resource registered successfully')
                    return redirect(project_profile, project.pk)

            except IntegrityError:
                # If the transaction failed
                messages.warning(request, 'There was an error saving the resource properties.')
                return render(request, template_name, locals())

    else:
        resource_form = ResourceForm()
        formset = formset_cls()
    return render(request, template_name, locals())


def get_resource_properties(request):
    if request.is_ajax():
        resource_id = request.POST.get('resource_id')
        resource = get_object_or_404(Resource, pk=resource_id)
        try:
            resource_properties = ResourceProperty.objects.filter(resource=resource)
        except ResourceProperty.DoesNotExist:
            resource_properties = None

        response_data = {}

        properties = []
        if resource_properties:
            for prop in resource_properties:
                resource_property = {}
                resource_property['name'] = prop.name
                resource_property['value'] = prop.value
                properties.append(resource_property)

        response_data['data'] = properties

        return JsonResponse(response_data)
