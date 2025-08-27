# WEEK 5
## Overview for activity 1

This Python library provides a simple implementation of a `Superhero` class and its subclass `FlyingSuperhero`. It demonstrates key object-oriented programming (OOP) concepts such as encapsulation (using private attributes and getter methods), inheritance (extending the base class), and polymorphism (overriding methods for different behavior).

The `Superhero` class represents a basic superhero with attributes like name, power, and strength. It includes methods to use their power and train to increase strength. The `FlyingSuperhero` subclass adds flying capabilities, showcasing how to build upon the base class.

## Classes

### Superhero

The base class for all superheroes.

#### Attributes (Encapsulated as Private)
- `_name`: The superhero's name (string).
- `_power`: The superhero's primary power (string).
- `_strength`: The superhero's strength level (integer).

#### Methods
- `__init__(self, name, power, strength)`: Constructor to initialize the superhero with unique values.
- `get_name(self)`: Getter method to retrieve the superhero's name (demonstrates encapsulation).
- `use_power(self)`: Prints a message showing the superhero using their power.
- `train(self)`: Increases the strength by 10 and prints the updated strength.

### FlyingSuperhero (Inherits from Superhero)

A subclass for superheroes who can fly, extending the base `Superhero` class.

#### Additional Attributes (Encapsulated as Private)
- `_flight_speed`: The flying speed in mph (integer).

#### Methods
- `__init__(self, name, power, strength, flight_speed)`: Constructor that calls the base class constructor and initializes the flight speed.
- `fly(self)`: Prints a message showing the superhero flying at their speed.
- `use_power(self)`: Overrides the base method to use the power and then fly (demonstrates polymorphism).

## Key OOP Concepts Demonstrated

- **Encapsulation**: Attributes are private (prefixed with `_`), and access is controlled via methods like `get_name()`. This hides internal details and promotes data integrity.
- **Inheritance**: `FlyingSuperhero` inherits attributes and methods from `Superhero` using `super().__init__()`, allowing code reuse.
- **Polymorphism**: The `use_power()` method behaves differently for `Superhero` and `FlyingSuperhero` instances, even when called through a common interface (e.g., in a loop over a list of heroes).
# Activity 2



## Overview
This Python script demonstrates object-oriented programming (OOP) concepts, specifically **inheritance** and **polymorphism**, by modeling different types of vehicles. Each vehicle type is represented by a class that inherits from a base `Vehicle` class and implements a `move` method to describe its unique movement behavior.

## Code Structure

### Classes
- **Vehicle**: The base class with a `move` method that is overridden by subclasses. It serves as an abstract template for all vehicle types.
- **Car**: Inherits from `Vehicle` and prints "Driving 🚗" when `move` is called.
- **Plane**: Inherits from `Vehicle` and prints "Flying ✈️" when `move` is called.
- **Boat**: Inherits from `Vehicle` and prints "Sailing 🛥️" when `move` is called.
- **Bike**: Inherits from `Vehicle` and prints "Pedaling 🚴" when `move` is called.
- **Train**: Inherits from `Vehicle` and prints "Chugging along 🚂" when `move` is called.

### Function
- **make_move(vehicle)**: A function that takes a `Vehicle` object as an argument and calls its `move` method. This showcases polymorphism, as the function can work with any subclass of `Vehicle`.

### Execution
- Instances of each vehicle type (`Car`, `Plane`, `Boat`, `Bike`, `Train`) are created.
- A list of vehicle instances is iterated over, and the `make_move` function is called for each, triggering the appropriate `move` behavior.

## How to Run
1. Ensure you have Python installed (version 3.x recommended).
2. Save the code in a file named `vehicle_simulation.py`.
3. Run the script using the command:
   ```bash
   python activity_2.py
   ```

## Output
When executed, the script will produce the following output:
```
Driving 🚗
Flying ✈️
Sailing 🛥️
Pedaling 🚴
Chugging along 🚂
```

## Purpose
This script serves as a simple example of:
- **Inheritance**: All vehicle classes inherit from the `Vehicle` base class.
- **Polymorphism**: The `make_move` function can call the `move` method on any `Vehicle` subclass, and the correct behavior is executed.
- **OOP Principles**: Demonstrates encapsulation of behavior in classes a   nd the use of method overriding.

## Notes
- The `Vehicle` class is designed as an abstract base class with a `pass` implementation of `move`. In a more advanced implementation, you could use the `abc` module to enforce abstraction.
- The script uses Unicode emojis to represent vehicles visually in the output.

## Licence
This project is licensed under the MIT License - feel free to use and modify it!

## Requirements

- Python 3.x
- No external libraries are required.
