def addCurlyBrackets(func):
	def wraper(data):
		return "{" + func(data) + "}"
	return wraper

def joinKeyAndValue(key, value):
	return '"{key}":"{value}"'.format(key=key, value=value)

@addCurlyBrackets
def dictToJson(data):
	return ",".join([ joinKeyAndValue(key, data[key]) for key in data])