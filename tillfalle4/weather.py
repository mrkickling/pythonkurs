import requests # så vi kan hämta hemsidor från internet
import datetime

# Be avändaren om en stad
stad = input("Skriv in en stad för att få vädret där:")
URL = "https://api.openweathermap.org/data/2.5/weather?q="+stad+"&appid=831c45d6783bf7371e3237d852d5daf8"
response = requests.get(URL)
weather_dict = response.json()

if weather_dict["cod"] != 200: # Något har gått fel
    print(weather_dict["message"])
else:
    description = weather_dict["weather"][0]["description"]
    main = weather_dict["weather"][0]["main"]
    temperatur = weather_dict["main"]["temp"]

    sunrise = weather_dict["sys"]["sunrise"]
    sunrise = datetime.datetime.fromtimestamp(sunrise)

    sunset = weather_dict["sys"]["sunset"]
    sunset = datetime.datetime.fromtimestamp(sunset)

    print("The weather in", stad, "is", main, description)
    print("Temperature is", round(temperatur-273, 1), "degrees celsius")
    print("Sunrise:", f"{sunrise:%H:%M}", "Sunset:", f"{sunset:%H:%M}")
