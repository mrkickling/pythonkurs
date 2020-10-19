import requests

# Finns ett paket som heter selenium
# Ett program som hämtar nyheter från svt nyheter

URL = "https://www.svt.se/"
response = requests.get(URL).text

sokord_innan = '<span class="nyh_teaser__heading-title">'
sokord_efter = '</span>'

# find hittar indexen för där rubriken börjar
rubrik_start = response.find(sokord_innan) + len(sokord_innan)
print("Rubriken börjar på index", rubrik_start)

rubrik_slut = response[rubrik_start:].find(sokord_efter)

print(response[rubrik_start:rubrik_start + rubrik_slut])
