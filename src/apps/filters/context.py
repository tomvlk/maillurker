from apps.filters.models import FilterSet


def add_global_context(request):
	return {
		'apps_filters': {
			'global_filters': FilterSet.objects.filter(is_active=True, is_global=True),
			'user_filters': []
		}
	}
