# -*- coding: utf-8 -*-
# (c) 2017 Tuomas Airaksinen
#
# This file is part of Serviceform.
#
# Serviceform is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Serviceform is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Serviceform.  If not, see <http://www.gnu.org/licenses/>.

from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .. import forms, models
from ..utils import clean_session
from ..views.decorators import serviceform


@serviceform
def password_login(request: HttpRequest, service_form: models.ServiceForm) -> HttpResponse:
    clean_session(request)
    password_form = forms.PasswordForm(service_form)

    if request.method == 'POST':
        password_form = forms.PasswordForm(service_form, request.POST)
        if password_form.is_valid():
            participant = models.Participant.objects.create(
                form_revision=service_form.current_revision)
            request.session['authenticated_participant'] = participant.pk
            return HttpResponseRedirect(reverse('contact_details'))

    return render(request, 'serviceform/login/password_login.html',
                  {'password_form': password_form, 'service_form': service_form})


@serviceform
def send_participant_email(request: HttpRequest, service_form: models.ServiceForm) -> HttpResponse:
    email_form = forms.ParticipantSendEmailForm(service_form, request)

    if request.method == 'POST':
        email_form = forms.ParticipantSendEmailForm(service_form, request, request.POST)
        if email_form.is_valid():
            email_form.save()
            return HttpResponseRedirect(
                reverse('send_participant_email', args=(service_form.slug,)))

    return render(request, 'serviceform/login/send_participant_auth_link.html',
                  {'email_form': email_form, 'service_form': service_form})


@serviceform
def send_responsible_email(request: HttpRequest, service_form: models.ServiceForm) -> HttpResponse:
    email_form = forms.ResponsibleSendEmailForm(service_form, request)

    if request.method == 'POST':
        email_form = forms.ResponsibleSendEmailForm(service_form, request, request.POST)
        if email_form.is_valid():
            email_form.save()
            return HttpResponseRedirect(
                reverse('send_responsible_email', args=(service_form.slug,)))

    return render(request, 'serviceform/login/send_responsible_auth_link.html',
                  {'email_form': email_form, 'service_form': service_form})
