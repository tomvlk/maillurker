from rest_framework import serializers

from apps.api.fields import Base64Field
from apps.filters.models import FilterSet, Rule
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
		fields = ('id', 'is_attachment', 'type', 'filename', 'charset', 'body', 'size')


class MessagePartSummarySerializer(serializers.ModelSerializer):
	class Meta:
		model = MessagePart
		fields = ('id', 'is_attachment', 'type', 'filename', 'charset', 'size')


class MessageSerializer(serializers.ModelSerializer):
	recipients_to = serializers.JSONField()
	recipients_cc = serializers.JSONField()
	recipients_bcc = serializers.JSONField()
	headers = serializers.JSONField()
	source = Base64Field()
	parts = MessagePartSummarySerializer(
		many=True,
		read_only=True
	)

	class Meta:
		model = Message
		fields = (
			'id', 'peer', 'port', 'sender_name', 'sender_address',
			'recipients_to', 'recipients_cc', 'recipients_bcc',
			'subject', 'size', 'type', 'headers',
			'source', 'parts'
		)


# API V1 Serializers
class FilterSetAdvancedSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(default=None, allow_null=True)
	name = serializers.CharField()
	created_by = serializers.PrimaryKeyRelatedField(read_only=True)
	is_global = serializers.BooleanField()
	is_active = serializers.BooleanField()
	icon = serializers.CharField(max_length=255)
	rules = serializers.HyperlinkedRelatedField(
		read_only=True,
		many=True,
		view_name='api:rules_single',
		lookup_field='pk',
		lookup_url_kwarg='identifier'
	)

	count = serializers.IntegerField(allow_null=True, default=None)

	class Meta:
		model = FilterSet
		fields = ('id', 'name', 'created_by', 'is_global', 'is_active', 'icon', 'count', 'rules')


class RuleAdvancedSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(default=None, allow_null=True)

	filter_set = serializers.HyperlinkedRelatedField(
		read_only=False,
		queryset=FilterSet.objects.all(),
		many=False,
		view_name='api:filters_single',
		lookup_field='pk',
		lookup_url_kwarg='identifier'
	)

	class Meta:
		model = Rule
		fields = ('id', 'field', 'operator', 'negate', 'value', 'filter_set')
