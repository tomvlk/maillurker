from rest_framework import serializers

from apps.filters.models import FilterSet
from apps.mails.models import Message, MessagePart


class FilterSetSerializer(serializers.ModelSerializer):
	name = serializers.CharField()
	created_by = serializers.PrimaryKeyRelatedField(read_only=True)
	is_global = serializers.BooleanField()
	is_active = serializers.BooleanField()
	icon = serializers.CharField(max_length=255)

	count = serializers.IntegerField(allow_null=True, default=None)

	class Meta:
		model = FilterSet
		fields = ('name', 'created_by', 'is_global', 'is_active', 'icon', 'count')


class MessagePartSerializer(serializers.ModelSerializer):
	class Meta:
		model = MessagePart
		fields = ('id',)


class MessageSerializer(serializers.ModelSerializer):
	recipients_to = serializers.JSONField()
	recipients_cc = serializers.JSONField()
	recipients_bcc = serializers.JSONField()
	headers = serializers.JSONField()
	parts = serializers.HyperlinkedRelatedField(many=True, view_name='api:parts_detail', lookup_url_kwarg='part_id',
												read_only=True)

	class Meta:
		model = Message
		fields = (
			'id', 'peer', 'port', 'sender_name', 'sender_address',
			'recipients_to', 'recipients_cc', 'recipients_bcc',
			'subject', 'size', 'type', 'headers',
			'parts'
		)
