import dictToJson
import jsonToDict


def convertJSON(func):
	def wraper(data):

		if(type(data) is dict):
			return func(dictToJson.dictToJson(data))
		elif(type(data) is str):
			return func(jsonToDict.jsonToDict(data))
		return func("Error data!")

	return wraper