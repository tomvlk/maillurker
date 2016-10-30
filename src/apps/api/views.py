from rest_framework import status
from rest_framework import views
from rest_framework.parsers import JSONParser
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


class MailsAction(views.APIView):
	def post(self, request, action, *args, **kwargs):
		if not 'items' in request.data:
			return Response(status=status.HTTP_400_BAD_REQUEST)

		body_items = request.data['items']
		items = list()
		try:
			for row in body_items:
				items.append(Message.objects.get(pk=int(row)))
		except Exception as e:
			print(e)
			return Response(status=status.HTTP_404_NOT_FOUND)

		if action == 'remove' and request.user.is_authenticated():
			for item in items:
				item.parts.all().delete()
				item.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)

		return Response(status=status.HTTP_400_BAD_REQUEST)


class MailsDownload(views.APIView):
	pass
