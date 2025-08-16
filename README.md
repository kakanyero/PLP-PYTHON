# WEEK-1
# Simple Python Calculator

A basic command-line calculator that performs arithmetic operations based on user input.

## Features

- Performs addition, subtraction, multiplication, and division
- Handles invalid operations gracefully
- Prevents division by zero errors
- Cleans user input automatically
- Displays results in a clear format

## How to Use

1. Run the program in a Python environment (Python 3.x required)
2. Enter the first number when prompted
3. Enter the second number when prompted
4. Choose an operation (+, -, *, /)
5. View the result

Example:
```
Enter the first number: 10
Enter the second number: 5
Enter the operation (+, -, *, /): +
10.0 + 5.0 = 15.0
```

## Error Handling

The program handles:
- Invalid operations (shows error message)
- Division by zero (shows error message)
- Non-numeric inputs (will raise ValueError)


## How to Run

Simply execute the Python file:
```bash
python week_1.py
```

## Possible Improvements

Future versions could include:
- Support for more operations (exponents, modulu
s)                                              - Continuous calculations (keeping previous result)
- Better handling of floating-point precision   - GUI interface

# WEEK-2


# List Operations in Python

This Python script demonstrates various list operations, including appending, inserting, extending, removing, sorting, and searching for elements.

## Code Overview

The script performs the following operations on a list named `my_list`:

1. **Creates an empty list**
2. **Appends elements** (`10, 20, 30, 40`)
3. **Inserts an element** (`15` at the second position)
4. **Extends the list** with `[50, 60, 70]`
5. **Removes the last element**
6. **Sorts the list** in ascending order
7. **Finds the index** of the value `30`

## Final Output

After executing all operations, the index of `30` is printed:

```python
Index of 30: 3
```

## How to Run

1. Save the script as week_2.py`.
2. Execute it using Python


#week 3


# Discount Calculator

This Python program defines a function `calculate_discount(price, discount_percent)` that calculates the final price of an item after applying a discount, provided the discount percentage is 20% or higher. It also includes a user interface to input the original price and discount percentage, then displays the final price.

## Function Description

### `calculate_discount(price, discount_percent)`
- **Parameters**:
  - `price`: A float or integer representing the original price of an item.
  - `discount_percent`: A float or integer representing the discount percentage.
- **Logic**:
  - If `discount_percent` is 20% or higher, the function calculates the discount amount and subtracts it from the original price.
  - If `discount_percent` is less than 20%, the original price is returned unchanged.
- **Returns**:
  - The final price after applying the discount (if applicable) as a float, rounded to two decimal places.

## Program Features

- Prompts the user to enter the original price and discount percentage.
- Validates user input to ensure:
  - Both inputs are numeric (can be converted to float).
  - Price is non-negative.
  - Discount percentage is between 0 and 100.
- Displays the final price after applying the discount (if discount_percent >= 20%) or the original price (if discount_percent < 20%).
- Handles invalid inputs gracefully with appropriate error messages.



## Requirements

- Python 3.x

## License

This project is open-source and free to use.
