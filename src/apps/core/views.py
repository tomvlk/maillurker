from django.shortcuts import redirect
from rest_framework.views import APIView


class PreferenceView(APIView):
	valid_attributes = {
		'fluid': {'type': bool, 'default': True}
	}

	def get(self, request, *args, **kwargs):
		pref_attribute = request.GET.get('attribute')
		pref_action = request.GET.get('action')
		next_url = request.GET.get('next', '/')
		if not next_url.startswith('/'):
			next_url = '/'

		if not pref_action or not pref_attribute:
			return redirect(next_url)

		attribute = self.valid_attributes.get(pref_attribute, False)
		if not attribute:
			return redirect(next_url)

		value = request.session.get('preference.{}'.format(pref_attribute), attribute['default'])

		if pref_action == 'toggle' and attribute['type'] == bool:
			value = False if value else True

		# Save attribute (TODO: Implement user saved attributes).
		request.session['preference.{}'.format(pref_attribute)] = value

		return redirect(next_url)
