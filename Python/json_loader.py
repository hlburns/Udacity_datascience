# APIs: Aplication programming interface
# REST representational state transfer 
# consider data wrangling course (if free)
import json
import requests

if __name__ =="main":
	url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=f803de707fea2b5033da9671b3e875cb&format=json'
	data = requests.get(url).textdat
	data = json.loads(data) #interpret json data like dictotionary!
	print data['topartists']['artist'][0]['name']
