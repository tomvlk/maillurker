from rest_framework import serializers

from apps.filters.models import FilterSet


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
