# from functools import wraps
import sys
sys.path.append('converter/')
import convertJson

dict1 = {"name": "Snikers #1", "price": 103.50, "image": "bg-01.jpg", "description": "This is very cool snikers. Nice colorfull and quality"}
str1 = "{'price': 103.5, 'name': 'Snikers #1', 'image': 'bg-01.jpg', 'description': 'This is very cool snikers. Nice colorfull and quality'}"

@convertJson.convertJSON
def doSmthWithData(data):
	print(type(data))
	return str(data)

print(doSmthWithData(str1))