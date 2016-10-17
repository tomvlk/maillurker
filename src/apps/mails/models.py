from django.db import models
from jsonfield import JSONField
from picklefield import PickledObjectField

from apps.core.models import BaseModel


class Message(BaseModel):

	peer = models.CharField(max_length=255)
	port = models.IntegerField(null=True, default=None)

	sender_name = models.CharField(max_length=255, null=True, default=None)
	sender_address = models.CharField(max_length=255)

	recipients_to = JSONField(null=True, default=None)
	recipients_cc = JSONField(null=True, default=None)
	recipients_bcc = JSONField(null=True, default=None)

	subject = models.TextField()

	source = models.BinaryField(null=True, default=None)

	size = models.IntegerField(null=True, default=None)

	type = models.TextField(null=True, default=None)

	headers = JSONField(null=True, default=None)


class MessagePart(BaseModel):
	message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='parts')

	is_attachment = models.BooleanField()

	type = models.TextField(null=True)

	filename = models.CharField(max_length=512, null=True)

	charset = models.CharField(max_length=255, null=True)

	body = models.BinaryField(null=True)

	size = models.IntegerField(null=True)
