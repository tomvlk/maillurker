
def fullname(o):
	if o.__class__.__name__ == 'type':
		return o.__module__ + "." + o.__name__
	return o.__module__ + "." + o.__class__.__name__
