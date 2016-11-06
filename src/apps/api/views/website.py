from rest_framework import permissions
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response

from apps.api.serializers import MessageSerializer, MessagePartSerializer
from apps.filters.models import FilterSet
from apps.mails.models import Message, MessagePart
from .. import serializers


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


class MailsDetail(views.APIView):
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def get(self, request, mail_id, *args, **kwargs):
		try:
			mail = Message.objects.get(pk=int(mail_id))
		except:
			return Response(data=None, status=status.HTTP_404_NOT_FOUND)

		return Response(data=MessageSerializer(mail, context={'request': request}).data, status=status.HTTP_200_OK)


class PartsDetail(views.APIView):
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def get(self, request, part_id, *args, **kwargs):
		try:
			part = MessagePart.objects.get(pk=int(part_id))
		except:
			return Response(data=None, status=status.HTTP_404_NOT_FOUND)

		return Response(data=MessagePartSerializer(part, context={'request': request}).data, status=status.HTTP_200_OK)
