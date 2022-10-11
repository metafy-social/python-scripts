import os,requests
from win10toast import ToastNotifier
from dotenv import load_dotenv
load_dotenv()

n = ToastNotifier()
city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+os.getenv("API_key")+"&units=metric"

r = requests.get(url,auth= (os.getenv("user"),os.getenv("password")))
r_dict = r.json()


current_temp = r_dict['main']['temp']

weather_desc = r_dict['weather'][0]['description']

temp = (str(current_temp))

desc = str(weather_desc)

result = "Current temperature is: " + temp + " Celsius in " + city+ ".\nCurrent weather condition is: " + desc
n.show_toast("Live Weather update: ",
			result, duration = 10)
