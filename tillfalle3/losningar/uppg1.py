# Gör ett program som ber användaren om ett filnamn och sedan
# skapar den filen (bestäm själv om du vill skriva något i filen)

filnamn = input("Filnamn: ")
f = open(filnamn,"w")

# Kommer du ihåg vad \n representerar för något?
f.write("valfritt")
f.close()