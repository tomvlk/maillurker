from django.views.generic import TemplateView
from django.shortcuts import render

from apps.mails.models import Message


class MailList(TemplateView):
	template_name = 'mails/list.html'
