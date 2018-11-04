import re

pattern = r"^([{])(.+)([}])$"
p_breckets = r"([^'].+[^'])"

def parceString(data, re_pattern, ind=0):
	match = re.search(re_pattern, data.strip())
	return match.group(ind)


def getParsedItems(data, re_pattern,ind):
	temp = parceString(data, re_pattern,ind)
	return temp.split(",")


def jsonToDict(data):
	result = {}
	temp = [];
	for value in getParsedItems(data, pattern, 2):
		temp = value.split(":")
		result[parceString(temp[0], p_breckets)] = parceString(temp[1], p_breckets)
	return result
