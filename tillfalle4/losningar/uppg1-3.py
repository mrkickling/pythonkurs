import requests

stad = input("Vilken stad vill du ha vädret från?: ")

URL = "https://api.openweathermap.org/data/2.5/weather?q="+ stad +"&appid=--------hemligt---------"
res = requests.get(URL)
weather_dict = res.json()
while weather_dict["cod"] == "404": # Om användaren skrev in en stad som inte finns
    stad = input("Pröva igen: ") # Fråga om staden igen
    URL = "https://api.openweathermap.org/data/2.5/weather?q="+ stad +"&appid=831c45d6783bf7371e3237d852d5daf8"
    res = requests.get(URL)
    weather_dict = res.json()

# hämta väderbeskrivningen i dictionaryn
weather_desc = weather_dict["weather"][0]["description"]
temperature = weather_dict["main"]["temp"]
print("The weather in", stad, "is", weather_desc)
print("The temperature in", stad, "is", round(temperature - 273, 2), "degrees celsius")

