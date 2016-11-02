import json
import logging

from django.conf import settings
from django.core.cache import cache
from django.db import models
from jsonfield import JSONField

from apps.core.models import BaseModel

logger = logging.getLogger(__name__)


class Message(BaseModel):

	peer = models.CharField(max_length=255)
	port = models.IntegerField(null=True, default=None)

	sender_name = models.CharField(max_length=255, null=True, default=None)
	sender_address = models.CharField(max_length=255)

	recipients_to = JSONField(null=True, default=None)
	recipients_cc = JSONField(null=True, default=None)
	recipients_bcc = JSONField(null=True, default=None)

	subject = models.TextField()

	source = models.TextField(null=True, default=None)

	size = models.IntegerField(null=True, default=None)

	type = models.TextField(null=True, default=None)

	headers = JSONField(null=True, default=None)


	@staticmethod
	def count_all():
		total = None
		try:
			if not settings.DEBUG and cache.get('mails.context.counts'):
				counts = json.loads(cache.get('mails.context.counts'))
				if 'total' in counts:
					total = counts['total']
		except Exception as e:
			logger.info('Can\'t retrieve or parse cache for message counts!')
			logger.debug(e)

		# Retrieve.
		if not total:
			total = Message.objects.count()

			if not settings.DEBUG:
				cache.set('mails.context.counts', json.dumps({
					'total': total
				}))

		return total

	@property
	def has_attachments(self):
		return len(self.parts.filter(is_attachment=True)) > 0

	@property
	def num_parts(self):
		return self.parts.count()

	@property
	def num_real_parts(self):
		return self.parts.exclude(type__contains='multipart').count()

	@property
	def eml(self):
		return self.source


class MessagePart(BaseModel):
	message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='parts')

	is_attachment = models.BooleanField()

	type = models.TextField(null=True)

	filename = models.CharField(max_length=512, null=True)

	charset = models.CharField(max_length=255, null=True)

	body = models.BinaryField(null=True)

	size = models.IntegerField(null=True)
