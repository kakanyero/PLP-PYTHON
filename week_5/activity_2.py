# Define a base class for Vehicles
class Vehicle:
    def move(self):
        pass

# Define classes for different types of vehicles
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

class Bike(Vehicle):
    def move(self):
        print("Pedaling 🚴")

class Train(Vehicle):
    def move(self):
        print("Chugging along 🚂")

# Create a function that takes an object and calls its move() method
def make_move(vehicle):
    vehicle.move()

# Create instances of vehicles
car = Car()
plane = Plane()
boat = Boat()
bike = Bike()
train = Train()

# Call the move() method on each instance
vehicles = [car, plane, boat, bike, train]
for vehicle in vehicles:
    make_move(vehicle)
