import importlib
import logging


logger = logging.getLogger(__name__)

BUTTONS = {
	'GoogleOAuth2': {
		'class': 'btn-google',
		'icon': 'fa fa-google',
		'text': 'Sign in with Google'
	},
	'GithubOAuth2': {
		'class': 'btn-github',
		'icon': 'fa fa-github',
		'text': 'Sign in with Github'
	},
	'BitbucketOAuth': {
		'class': 'btn-bitbucket',
		'icon': 'fa fa-bitbucket',
		'text': 'Sign in with Bitbucket'
	},
	'DropboxOAuth': {
		'class': 'btn-dropbox',
		'icon': 'fa fa-dropbox',
		'text': 'Sign in with Dropbox'
	},
	'FacebookOAuth2': {
		'class': 'btn-facebook',
		'icon': 'fa fa-facebook',
		'text': 'Sign in with Facebook'
	},
	'FlickrOAuth': {
		'class': 'btn-flickr',
		'icon': 'fa fa-flickr',
		'text': 'Sign in with Flickr'
	},
	'FoursquareOAuth2': {
		'class': 'btn-foursquare',
		'icon': 'fa fa-foursquare',
		'text': 'Sign in with Foursquare'
	},
	'InstagramOAuth2': {
		'class': 'btn-instagram',
		'icon': 'fa fa-instagram',
		'text': 'Sign in with Instagram'
	},
	'LiveOAuth2': {
		'class': 'btn-microsoft',
		'icon': 'fa fa-windows',
		'text': 'Sign in with Microsoft'
	},
	'LinkedinOAuth2': {
		'class': 'btn-linkedin',
		'icon': 'fa fa-linkedin',
		'text': 'Sign in with LinkedIn'
	},
	'OdnoklassnikiOAuth2': {
		'class': 'btn-odnoklassniki',
		'icon': 'fa fa-odnoklassniki',
		'text': 'Sign in with Odnoklassniki'
	},
	'OpenIdAuth': {
		'class': 'btn-openid',
		'icon': 'fa fa-openid',
		'text': 'Sign in with OpenID'
	},
	'RedditOAuth2': {
		'class': 'btn-reddit',
		'icon': 'fa fa-reddit',
		'text': 'Sign in with Reddit'
	},
	'SoundcloudOAuth2': {
		'class': 'btn-soundcloud',
		'icon': 'fa fa-soundcloud',
		'text': 'Sign in with Soundcloud'
	},
	'TumblrOAuth': {
		'class': 'btn-tumblr',
		'icon': 'fa fa-tumblr',
		'text': 'Sign in with Tumblr'
	},
	'TwitterOAuth': {
		'class': 'btn-twitter',
		'icon': 'fa fa-twitter',
		'text': 'Sign in with Twitter'
	},
	'VKOAuth2': {
		'class': 'btn-vk',
		'icon': 'fa fa-vk',
		'text': 'Sign in with VK'
	},
	'YahooOAuth': {
		'class': 'btn-yahoo',
		'icon': 'fa fa-yahoo',
		'text': 'Sign in with Yahoo'
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
	module_name = backend[0:(str(backend).rindex('.'))]
	class_name = backend[(len(module_name) + 1):]
	module = importlib.import_module(module_name)
	clazz = getattr(module, class_name)
	name = getattr(clazz, 'name', class_name)

	infos = {
		'class': False,
		'icon': False,
		'code': name,
		'text': name
	}

	if class_name in BUTTONS:
		infos = BUTTONS[class_name]
		infos['code'] = name
	else:
		logger.debug('We don\'t know the right button info and styling for the enabled social backend \'{}\''.format(
			backend
		))

	return infos
