from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from .forms import RegistrationForm, LoginForm


def registration(request):
    page_title = 'User Registration'
    template_name = 'user_account/register.html'
    has_account = False

    if request.user.is_authenticated():
        has_account = True
        messages.warning(request, _(
            'Sorry, {0}. This service is only for registration of new users')
            .format(request.user.username))
        # redirect to homepage...
        return redirect(home)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if request.POST.get('cancel', None):
            return redirect(home)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)

            user.is_active = False
            user.first_name = first_name.upper()
            user.last_name = last_name.upper()
            user.save()
            return redirect(success, pk=user.pk)
        else:
            msg = ("Ooops! Please correct the highlighted fields,"
                   " then try again.")
            messages.warning(request, _(msg))
            return render(request, template_name, locals())
    else:
        form = RegistrationForm()
        return render(request, template_name, locals())


def home(request):
    template_name = 'user_account/home.html'
    page_title = 'Single Point Of Truth'
    return render(request, template_name, locals())


def LoginRequest(request):
    template_name = 'user_account/login.html'

    if request.user.is_authenticated():
        return redirect(home)

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            siteuser = authenticate(username=username, password=password)

            if siteuser is not None:
                """set a session id for this session"""
                login(request, siteuser)
                messages.info(request, 'Welcome, {0}'.format(
                              siteuser.last_name + ' ' + siteuser.first_name))
                return redirect(home)
            else:
                msg = ("Sorry, the login credentials you've provided"
                       " don't match any user account.")
            messages.warning(request, _(msg))
        else:
            msg = ("Ooops! Please correct the highlighted"
                   " fields, then try again.")
            messages.warning(request, _(msg))
    else:
        form = LoginForm()
    return render(request, template_name, locals())


def LogoutRequest(request):
    '''expires the session'''
    logout(request)
    return redirect(LoginRequest)


def success(request, pk):
    user = User.objects.get(pk=pk)
    template_name = 'user_account/success.html'
    page_title = 'Successful Registration'
    user.is_authenticated = False
    return render(request, template_name, locals())
