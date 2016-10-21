from rest_framework import views
from rest_framework.response import Response

from apps.filters.models import FilterSet
from apps.mails.models import Message
from . import serializers


class RealTimeInfos(views.APIView):

	def get(self, request):

		global_filters = FilterSet.objects.filter(is_global=True, is_active=True)

		personal_filters = list()
		if request.user.is_authenticated():
			personal_filters = FilterSet.objects.filter(is_global=False, is_active=True, created_by=request.user)

		print(personal_filters)

		data = {
			'filters': {
				'global': serializers.FilterSetSerializer(global_filters, many=True).data,
				'personal': serializers.FilterSetSerializer(personal_filters, many=True).data,
			},
			'total_emails': Message.count_all()
		}

		return Response(data)
