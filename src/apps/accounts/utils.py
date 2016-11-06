import importlib
import logging


logger = logging.getLogger(__name__)

BUTTONS = {
	'GoogleOAuth2': {
		'class': 'btn-google',
		'icon': 'fa fa-google',
		'name': 'Google'
	},
	'GithubOAuth2': {
		'class': 'btn-github',
		'icon': 'fa fa-github',
		'name': 'Github'
	},
	'BitbucketOAuth': {
		'class': 'btn-bitbucket',
		'icon': 'fa fa-bitbucket',
		'name': 'Bitbucket'
	},
	'DropboxOAuth': {
		'class': 'btn-dropbox',
		'icon': 'fa fa-dropbox',
		'name': 'Dropbox'
	},
	'FacebookOAuth2': {
		'class': 'btn-facebook',
		'icon': 'fa fa-facebook',
		'name': 'Facebook'
	},
	'FlickrOAuth': {
		'class': 'btn-flickr',
		'icon': 'fa fa-flickr',
		'name': 'Flickr'
	},
	'FoursquareOAuth2': {
		'class': 'btn-foursquare',
		'icon': 'fa fa-foursquare',
		'name': 'Foursquare'
	},
	'InstagramOAuth2': {
		'class': 'btn-instagram',
		'icon': 'fa fa-instagram',
		'name': 'Instagram'
	},
	'LiveOAuth2': {
		'class': 'btn-microsoft',
		'icon': 'fa fa-windows',
		'name': 'Microsoft'
	},
	'LinkedinOAuth2': {
		'class': 'btn-linkedin',
		'icon': 'fa fa-linkedin',
		'name': 'LinkedIn'
	},
	'OdnoklassnikiOAuth2': {
		'class': 'btn-odnoklassniki',
		'icon': 'fa fa-odnoklassniki',
		'name': 'Odnoklassniki'
	},
	'OpenIdAuth': {
		'class': 'btn-openid',
		'icon': 'fa fa-openid',
		'name': 'OpenID'
	},
	'RedditOAuth2': {
		'class': 'btn-reddit',
		'icon': 'fa fa-reddit',
		'name': 'Reddit'
	},
	'SoundcloudOAuth2': {
		'class': 'btn-soundcloud',
		'icon': 'fa fa-soundcloud',
		'name': 'Soundcloud'
	},
	'TumblrOAuth': {
		'class': 'btn-tumblr',
		'icon': 'fa fa-tumblr',
		'name': 'Tumblr'
	},
	'TwitterOAuth': {
		'class': 'btn-twitter',
		'icon': 'fa fa-twitter',
		'name': 'Twitter'
	},
	'VKOAuth2': {
		'class': 'btn-vk',
		'icon': 'fa fa-vk',
		'name': 'VK'
	},
	'YahooOAuth': {
		'class': 'btn-yahoo',
		'icon': 'fa fa-yahoo',
		'name': 'Yahoo'
	}
}
# Add double references
BUTTONS['DropboxOAuth2'] = BUTTONS['DropboxOAuth']
BUTTONS['FacebookAppOAuth2'] = BUTTONS['FacebookOAuth2']
BUTTONS['GoogleOAuth'] = BUTTONS['GoogleOAuth2']
BUTTONS['GoogleOpenId'] = BUTTONS['GoogleOAuth2']
BUTTONS['GooglePlusAuth'] = BUTTONS['GoogleOAuth2']
BUTTONS['GoogleOpenIdConnect'] = BUTTONS['GoogleOAuth2']
BUTTONS['LinkedinOAuth'] = BUTTONS['LinkedinOAuth2']
BUTTONS['YahooOpenId'] = BUTTONS['YahooOAuth']
BUTTONS['BitbucketOAuth2'] = BUTTONS['BitbucketOAuth']


def get_social_button(backend):
	"""
	Get button infos for given backend package+class.
	:param backend:
	:return:
	"""

	if type(backend) is str:
		module_name = backend[0:(str(backend).rindex('.'))]
		class_name = backend[(len(module_name) + 1):]
		module = importlib.import_module(module_name)
		clazz = getattr(module, class_name)
		name = getattr(clazz, 'name', class_name)
	else:
		raise Exception('Can\'t yet get from class instance!')

	infos = {
		'class': False,
		'icon': False,
		'code': name,
		'text': 'Sign in with {}'.format(name),
		'name': name
	}

	if class_name in BUTTONS:
		infos = BUTTONS[class_name]
		infos['text'] = 'Sign in with {}'.format(infos['name'])
		infos['code'] = name
	else:
		logger.debug('We don\'t know the right button info and styling for the enabled social backend \'{}\''.format(
			backend
		))

	return infos
