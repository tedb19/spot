from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.http import JsonResponse

from user_account.views import LoginRequest
from resources.models import Resource
from .models import Project
from .forms import ProjectForm


def projects_listing(request):
    if not request.user.is_authenticated:
        return redirect(LoginRequest)
    page_title = 'Projects'
    template_name = 'project/projects_listing.html'
    projects = Project.objects.all()
    project_ = {}
    # "name": "", "pk": "", "description": ""
    projects_ = []
    for project in projects:
        project_["name"] = project.name
        project_["pk"] = project.pk
        project_["description"] = project.description
        project_["length"] = len(project.description.split(" "))
        projects_.append(project_)
    return render(request, template_name, locals())


def project_profile(request, project_id):
    if not request.user.is_authenticated:
        return redirect(LoginRequest)
    template_name = 'project/project_profile.html'
    project = get_object_or_404(Project, pk=project_id)
    try:
        resources = Resource.objects.filter(project=project)
    except Resource.DoesNotExist:
        resources = None
    page_title = project.name
    return render(request, template_name, locals())


def project_registration(request):
    if not request.user.is_authenticated:
        return redirect(LoginRequest)
    page_title = 'Project Registration'
    template_name = 'project/project_registration.html'
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if request.POST.get('cancel', None):
            return redirect(projects_listing)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            project = Project.objects.create(name=name, description=description)
            messages.info(request, '{0} project registered successfully'.format(name))
            return redirect(projects_listing)
        else:
            msg = ("Ooops! Please correct the highlighted fields,"
                   " then try again.")
            messages.warning(request, _(msg))
            return render(request, template_name, locals())
    else:
        form = ProjectForm()
        return render(request, template_name, locals())
