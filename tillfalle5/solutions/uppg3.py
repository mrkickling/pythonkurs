# Utveckla programmet som sade vädret i en specifik stad till att skriva ut
# mer än bara en beskrivning av vädret (t.ex. temperatur, solens upp- och nedgång)
# Programmet kräver paketet "requests"
# Länken till openweathermap kanske inte funkar om du kör det här programmet långt efter december 2019

import requests
from datetime import datetime

while True: # Fortsätt fråga om stad i all oändlighet
    city = input("City (or 'quit' to quit): ")
    if city == "quit": # Användaren avslutar programmet genom att skriva "quit"
        break

    URL = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=831c45d6783bf7371e3237d852d5daf8"
    response = requests.get(URL)
    weather_dict = response.json()

    if weather_dict['cod'] == "404": # Error, no city found
        print("No city found")
        continue

    # Hämta väderbeskrivning och landkod
    weather_description = weather_dict['weather'][0]['description']
    country_code = weather_dict["sys"]["country"]

    # Hämta solens upp och nedgång i UNIX-tid-format
    sunrise_unix_timestamp = int(weather_dict["sys"]["sunrise"])
    sunset_unix_timestamp = int(weather_dict["sys"]["sunset"])

    # Omvandla till läsbart format för människor TIMME:MINUT:SEKUND
    # Tiden kommer vara i UTC, alltså en timma fel, eller kanske två? Det får funka.
    sunrise_hour_minute = datetime.utcfromtimestamp(sunrise_unix_timestamp).strftime('%H:%M:%S')
    sunset_hour_minute = datetime.utcfromtimestamp(sunset_unix_timestamp).strftime('%H:%M:%S')

    # Printa ut all information
    print("The weather in " + city + " is " + weather_description + ". Sun will rise at " + sunrise_hour_minute +
        " and set at " + sunset_hour_minute)
