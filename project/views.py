from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.http import JsonResponse

from user_account.views import LoginRequest
from .models import Project
from .forms import ProjectForm


def projects_listing(request):
    if not request.user.is_authenticated:
        return redirect(LoginRequest)
    page_title = 'Projects'
    template_name = 'project/projects_listing.html'
    projects = Project.objects.all()
    return render(request, template_name, locals())


def project_registration(request):
    if not request.user.is_authenticated:
        return redirect(LoginRequest)
    page_title = 'Project Registration'
    template_name = 'project/project_registration.html'
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if request.POST.get('cancel', None):
            return redirect(home)
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
