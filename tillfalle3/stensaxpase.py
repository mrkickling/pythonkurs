import random
alternatives = ["Sten", "Sax", "Påse"]

computer_guess = alternatives[random.randrange(3)]
user_guess = input("Sten, Sax eller Påse? ")
if user_guess == computer_guess:
    print("Oavgjort! Ni valde båda " + computer_guess)
elif user_guess == "Sten":
    if computer_guess == "Sax":
        print("Du vinner med " + user_guess + " mot " + computer_guess)
    else:
        print("Du förlorar med " + user_guess + " mot " + computer_guess)
elif user_guess == "Sax":
    if computer_guess == "Påse":
        print("Du vinner med " + user_guess + " mot " + computer_guess)
    else:
        print("Du förlorar med " + user_guess + " mot " + computer_guess)
elif user_guess == "Påse":
    if computer_guess == "Sten":
        print("Du vinner med " + user_guess + " mot " + computer_guess)
    else:
        print("Du förlorar med " + user_guess + " mot " + computer_guess)
