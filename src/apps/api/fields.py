import base64

from rest_framework import serializers


class Base64Field(serializers.Field):
	def to_representation(self, obj):
		return base64.b64encode(obj.encode('utf-8'))

	def to_internal_value(self, data):
		return base64.b64decode(data).decode('utf-8')
