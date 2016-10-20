import sys
import os
import smtplib

from django.conf import settings

EML_SERVER = '127.0.0.1'
EML_PORT = '1025'
EML_ROOT = os.path.join(settings.TEST_DIR, 'files', 'eml')


def send_eml(path, from_addr, to_addrs, mail_options=None, rcpt_options=None):
	"""
	Send mail from EML file.
	:param path:
	:param from_addr:
	:param to_addrs:
	:param mail_options:
	:param rcpt_options:
	:return:
	"""
	if rcpt_options is None:
		rcpt_options = []
	if mail_options is None:
		mail_options = []

	if not os.path.isabs(path):
		path = os.path.join(EML_ROOT, path)

	if not os.path.isfile(path):
		raise Exception('EML file \'{}\' doesn\'t exists!'.format(path))

	with open(path) as emlfile:
		msg = emlfile.read()

	smtp = None
	try:
		smtp = smtplib.SMTP(EML_SERVER, EML_PORT)
		smtp.sendmail(from_addr, to_addrs, msg, mail_options, rcpt_options)
	except Exception as e:
		smtp.close()
		raise e
	finally:
		smtp.close()
	return True
