import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

loc = str(input("Enter Location : "))
url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":loc}

headers = {
	"X-RapidAPI-Key": WEATHER_API_KEY,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_str = json.dumps(response.text)
y = json.loads(response.text)
print(
"\n\n",
"------------------------------------------\n",
"Name : ", y["location"]["name"], "\n", 
"Region : " , y["location"]["region"], "\n", 
"Country : " , y["location"]["country"], "\n", 
"Latitude : " , y["location"]["lat"], "\n", 
"Longitude : " , y["location"]["lon"], "\n", 
"------------------------------------------\n",
"Temeperature : " , y["current"]["temp_c"], "°C\n", 
"Wind Speed : " , y["current"]["wind_kph"], "kmh\n", 
"Wind Degree : " , y["current"]["wind_degree"], "°\n", 
"Wind Direction : " , y["current"]["wind_dir"], "\n",
"------------------------------------------\n"
)
