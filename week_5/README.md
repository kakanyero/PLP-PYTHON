# WEEK 5
## Overview

This Python library provides a simple implementation of a `Superhero` class and its subclass `FlyingSuperhero`. It demonstrates key object-oriented programming (OOP) concepts such as encapsulation (using private attributes and getter methods), inheritance (extending the base class), and polymorphism (overriding methods for different behavior).

The `Superhero` class represents a basic superhero with attributes like name, power, and strength. It includes methods to use their power and train to increase strength. The `FlyingSuperhero` subclass adds flying capabilities, showcasing how to build upon the base class.

## Requirements

- Python 3.x

No external dependencies are required.

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

## License

This project is licensed under the MIT License - feel free to use and modify it!
