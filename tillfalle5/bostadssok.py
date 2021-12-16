import requests
 
URL = "https://bostad.stockholm.se/Lista/AllaAnnonser"
 
res = requests.get(URL)
res = res.json()
 
maxhyra = int(input("Maxhyra: "))
minantalrum = int(input("Minst antal rum: "))
minyta = int(input("Minsta yta: "))
 
for bostad in res:
    stadsdel = bostad["Stadsdel"]
    adress = bostad["Gatuadress"]
    kommun = bostad["Kommun"]
    vaning = bostad["Vaning"]
    antalrum = bostad["AntalRum"]
    yta = bostad["Yta"]
    hyra = bostad["Hyra"]
    if hyra == None or antalrum == None or yta == None:
        continue
    if hyra <= maxhyra and antalrum >= minantalrum and yta >= minyta:
        print(
            stadsdel,
            antalrum, "rum.",
            yta,"kvm.",
            hyra, "kr / månad"
        ) 
