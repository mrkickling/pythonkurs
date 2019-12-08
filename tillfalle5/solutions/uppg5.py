# Skapa ett program som ber användaren om en hållplats inom SL
# och printar ut infomation om alla nästkommande avgångar (buss/tunnelbana/pendel).
# Använd trafiklab.ses API:er SL Platsuppslag och SL Realtidsinformation 4.

# Kräver installation av paketet 'requests'
import requests
API_NYCKEL_PLATSUPPSLAG = "<NYCKEL>" # Skriv in din nyckel från trafiklab.se
API_NYCKEL_REALTIDSINFORMATION4 = "<NYCKEL>" # Skriv in din nyckel från trafiklab.se här

# Först ber vi användaren om en hållplats
hallplats = input("Hållplats: ")

# Sen hämtar vi ID-numret för den hållplatsen från Platsuppslag
URL = "https://api.sl.se/api2/typeahead.json?key=" + API_NYCKEL_PLATSUPPSLAG + "&searchstring=" + hallplats +"&stationsonly=True&maxresults=1"
response = requests.get(URL)
response_dictionary = response.json()["ResponseData"]
hallplats_ID = response_dictionary[0]["SiteId"] # ID:t som vi nu kan använda i nästa API-request

# Nu hämtar vi nästkommande anvångarna från Realtidsinformation 4. Ändra time window vid behov, nu på 5 minuter.
URL2 = "https://api.sl.se/api2/realtimedeparturesV4.json?key=" + API_NYCKEL_REALTIDSINFORMATION4 + "&siteid=" + hallplats_ID + "&timewindow=10"
response2 = requests.get(URL2)

if response2.json()["StatusCode"] > 0: # avbryt om det kommer en felkod
    print("Error! Try again.")
else:
    nastkommande_avgangar = response2.json()["ResponseData"]
    nastkommande_tunnelbanor = nastkommande_avgangar["Metros"]

    for avgang in nastkommande_tunnelbanor:
        print(avgang["Destination"] + ": " + avgang["DisplayTime"])
