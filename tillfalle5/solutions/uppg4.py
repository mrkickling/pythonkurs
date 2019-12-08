# Utveckla Car-classen, så att den har en egenskap “speed” som kan ökas med metoden “increase_speed”
# och minskas med metoden “decrease_speed”. Ökas = adderas
class Car:
    def __init__(self, license_plate, owner, color):
        self.license_plate = license_plate
        self.owner = owner
        self.color = color
        self.speed = 0

    def print_car_info(self):
        print(" -- " + self.license_plate + " -- ")
        print("  Owner: " + self.owner )
        print("  Color" + self.color )

    def increase_speed(self):
        self.speed += 10

    def decrease_speed(self):
        self.speed -= 10

    def show_speed(self):
        print("Your speed is " + str(self.speed) )

car1 = Car("ABC123", "Joakim Loxdal", "Blue")
car1.show_speed();
car1.increase_speed();
car1.show_speed();
