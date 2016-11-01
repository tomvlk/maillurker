import math
import os
import zipfile

from io import BytesIO

from django.db.models import Q
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.response import Response

from apps.filters.models import FilterSet
from apps.mails.models import Message


class MailList(TemplateView):
	template_name = 'mails/list.html'
	sortable_columns = {
		'from': 'sender_address',
		'to': 'recipients_to',
		'subject': 'subject',
		'size': 'size',
		'received': 'created_at',
	}

	def get_context_data(self, **kwargs):
		# Search
		search = self.request.GET.get('q', False)

		if not search:
			search = None

		# Sort & Order
		sort = self.request.GET.get('sort', 'received')
		order = self.request.GET.get('order', 'desc')

		if not self.sortable_columns.get(sort, None):
			sort = 'received'
			order = 'desc'

		if not order == 'asc' and not order == 'desc':
			order = 'asc'

		sort_field = self.sortable_columns.get(sort)

		filterset = None
		if 'filter_id' in kwargs:
			try:
				filterset = FilterSet.objects.get(pk=kwargs['filter_id'])
			except:
				pass

			# Check if user has rights to access the filter set.
			if filterset and not filterset.is_global:
				if not self.request.user.is_authenticated() or not getattr(self.request.user, 'is_superuser', False) \
					or not filterset.created_by_id != self.request.user.pk:
					filterset = None

		if not filterset:
			mails = Message.objects.all()
		else:
			mails = filterset.get_matches()

		# Apply order.
		mails = mails.order_by('{}{}'.format('-' if order == 'desc' else '', sort_field))

		# Searching
		if search:
			mails = mails.filter(
				Q(subject__icontains=search) |
				Q(sender_name__icontains=search) |
				Q(sender_address__icontains=search) |
				Q(recipients_to__icontains=search) |
				Q(peer__icontains=search) |
				Q(size__icontains=search) |
				Q(source__icontains=search)
			)

		# Pagination.
		total = mails.count()
		per_page = int(self.request.GET.get('max', 40))
		page = int(self.request.GET.get('page', 1))

		if type(per_page) is not int or per_page < 1 or per_page > 1000:
			per_page = 40

		pages = int(math.ceil(total / per_page))

		prev = True if page > 1 else False
		next = False if page >= pages else True
		display = list()
		if page <= 5 and pages >= 10:
			display = list(range(1, 11))
		elif page <= 5 and pages < 10:
			display = list(range(1, pages))

		elif page > 5 and pages >= (page + 4):
			display = list(range((page - 5), (page + 5)))
		elif page > 5 and pages >= page:
			display = list(range((page - 5), (pages + 1)))
		else:
			display = list(page)

		offset = (page - 1) * per_page
		limit = offset + per_page

		mails = mails[offset:limit]

		return {
			'list': mails,
			'sort': sort,
			'order': order,
			'pagination': {
				'prev': prev,
				'next': next,
				'page': page,
				'prev_page': page - 1,
				'next_page': page + 1,
				'rows': total,
				'pages': pages,
				'display': display
			},
			'search_text': '' if not search else search,
			'actionbar': True
		}


class MailDownload(View):

	def get(self, request, mail_ids):
		mail_ids = mail_ids.split(',')
		stream = BytesIO()
		zf = zipfile.ZipFile(stream, 'w')

		for idx in mail_ids:
			mail = Message.objects.get(pk=int(idx))
			zf.writestr(zinfo_or_arcname='mail-{}.eml'.format(int(idx)), data=mail.eml)

		zf.close()
		resp = HttpResponse(stream.getvalue(), content_type='application/x-zip-compressed')
		resp['Content-Disposition'] = 'attachment; filename={}'.format('emails.zip')

		return resp


class MailDetail(View):

	def get(self, request, mail_id):

		return Response()
