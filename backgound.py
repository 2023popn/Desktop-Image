import requests
import json
import webbrowser
import os
import urllib
from appscript import app, mactypes
from datetime import date
from datetime import timedelta

today = date.today()

image_dir = '/Users/2023popn/Downloads/ImagesForBackground'

def get_image_from_date(date):
	
	date_api_link = "https://api.nasa.gov/planetary/apod?api_key=TjfoieB4nVydTsQZ8FspJmm6cnG1oqd7gOM1DV9R&date=" + str(date)

	data = requests.get(date_api_link)
	data_json = json.loads(data.text)

	if(str(data_json["url"])[-4:] == ".jpg"):
		full_file_name = os.path.join(image_dir, data_json['url'])

		for file in os.listdir(image_dir):
			os.remove(os.path.join(image_dir, file))

		save_to_file = image_dir + '/todays_image' + str(today) + '.jpg'

		urllib.request.urlretrieve(data_json['url'], save_to_file)
	else:
		get_image_from_date(date - timedelta(days = 1))

get_image_from_date(today)
