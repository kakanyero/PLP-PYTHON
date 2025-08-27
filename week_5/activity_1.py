class Superhero:
    def __init__(self, name, power, strength):
        self._name = name          # Private attribute for encapsulation
        self._power = power        # Private attribute
        self._strength = strength  # Private attribute

    def get_name(self):            # Getter method for encapsulation
        return self._name

    def use_power(self):
        print(f"{self._name} uses {self._power}!")

    def train(self):
        self._strength += 10
        print(f"{self._name} trained! Strength now: {self._strength}")

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength, flight_speed):
        super().__init__(name, power, strength)  # Call base class constructor
        self._flight_speed = flight_speed        # Additional private attribute

    def fly(self):
        print(f"{self._name} flies at {self._flight_speed} mph!")

    def use_power(self):  # Overridden method for polymorphism
        super().use_power()  # Call base class method
        self.fly()
