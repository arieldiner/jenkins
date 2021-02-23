

from pprint import pprint
import requests
import json 

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Tel-aviv&units=metric&APPID=4265b7ed4ce93d37f19589f7324b4cfb')
print ("Hello Iguazio")
print ("The weather in Tel-Aviv is:" + str(json.loads(json.dumps(r.json()))['main']['temp']) + " Celsius")
