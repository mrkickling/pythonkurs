import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Stockholm&appid=831c45d6783bf7371e3237d852d5daf8")
weather_dict = response.json()
weather_description = weather_dict['weather'][0]['description']

print("The weather in Stockholm is " + weather_description)
