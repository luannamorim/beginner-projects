import requests
from pprint import pprint


API_Key = 'fd604c9a3f541868b248e4b32752444d'
city = input("Enter a city: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_Key
weather_data = requests.get(base_url).json()
