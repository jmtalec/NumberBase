# NumberBase Module Readme

## Overview

`NumberBase` is a custom Python class that represents integers in different bases, allowing for operations such as addition, subtraction, and multiplication while retaining the base of the number. This class extends the built-in `int` type and provides a way to work with numbers in various bases, like binary, decimal, and hexadecimal, as well as user-defined bases.

## Features

- **Base conversion:** Convert integers to different bases, such as binary, decimal, or custom bases.
- **Base-preserving arithmetic operations:** Perform arithmetic operations (`+`, `-`, `*`, etc.) while retaining the original base of the numbers.
- **Immutable properties:** Certain properties like `base`, `base_map`, and `null` are immutable after the object is created.
- **String representation:** Customize the string and repr representation of the number based on its base.

## Installation

This module is intended to be integrated directly into a Python project. No external dependencies are needed beyond the standard Python library.

## Usage

### Import and Initialization

To use `NumberBase`, import the class and create an instance by providing an integer and a base mapping. The base mapping can be one of the predefined bases (decimal, binary, hexadecimal) or a custom iterable that defines the symbols used for that base.

```python
from string import digits, ascii_lowercase
from enum import Enum

# Example of creating a NumberBase instance with a custom base map
num = NumberBase(3453, digits + "ABCDEF")
```

### Example Operations

The `NumberBase` class supports all common arithmetic operations like addition, subtraction, multiplication, and more, while retaining the base of the original number.

```python
# Define a number in a custom hexadecimal-like base
num = NumberBase(3453, digits + "ABCDEF")

# Print the representation of the number in the custom base
print(repr(num))  # Output: [bn]: D7D

# Adding 1 to the number while retaining the base
result = num + 1
print(repr(result))  # Output: [bn]: D7E
```

### Custom Bases

You can define custom bases by passing an iterable that represents the symbols for that base:

```python
# Binary number (Base 2)
binary_num = NumberBase(25, [0, 1])
print(binary_num)  # Output: binary representation of 25
print(binary_num + 1)  # Output: binary representation of 26
```

### Enum-Based Bases

You can also use the provided `Bases` enum to initialize `NumberBase` instances with predefined bases:

```python
from enum import Enum

class Bases(Enum):
    DECIMAL = "0123456789"
    BINARY  = "01"
    HEXADECIMAL = "0123456789ABCDEF"

hex_num = NumberBase(255, Bases.HEXADECIMAL)
print(hex_num)  # Output: FF (in hexadecimal)
```

## Class Details

### `NumberBase` Class

- **Attributes:**
  - `base`: The length of the base map (number of symbols in the base).
  - `base_map`: A tuple of symbols representing the base.
  - `null`: The symbol representing zero in the base.

- **Methods:**
  - `to_base(base_map: Union[Iterable[object], Bases], null: object=None)`: Initializes a new instance of `self` with the specified base and null value.
  - `__new__(cls, x: int, base_map: Union[Iterable[object], Bases], null: object = None)`: Creates the integer instance.
  - `__init__(self, x: int, base_map: Union[Iterable[object], Bases], null: object = None)`: Initializes the instance with the specified base and null value.
  - `__add__`, `__sub__`, `__mul__`, etc.: Arithmetic operations that preserve the base of the `NumberBase` instance.
  - `__repr__()`: Returns a custom string representation of the number in its base.

### Base Operations

The `NumberBase` class implements most arithmetic and bitwise operations (`+`, `-`, `*`, `/`, `//`, `%`, `&`, `|`, `^`, `<<`, `>>`) while ensuring that the base is preserved. Operations between two `NumberBase` instances or between a `NumberBase` and a regular integer are supported.

For instance, adding an integer to a `NumberBase` object returns a new `NumberBase` object with the result converted back to the original base.

### Immutability

Once a `NumberBase` instance is initialized, certain attributes (`base`, `base_map`, `null`) cannot be modified or deleted. Attempts to do so will raise an `AttributeError`.

```python
num = NumberBase(10, Bases.DECIMAL)
num.base = 2  # Raises AttributeError: The 'base' attribute is immutable
```

### String Representation

The `__str__()` and `__repr__()` methods provide custom representations of `NumberBase` objects. The `__str__()` method returns the number as a string in its respective base, while `__repr__()` prefixes the output with `[bn]:`.

```python
print(str(num))  # Example output: D7D
print(repr(num))  # Example output: [bn]: D7D
```

## Future Enhancements

- **Support for fractional numbers:** Extend `NumberBase` to handle floating-point numbers.
- **Custom formatting options:** Allow customization of the `repr` and `str` outputs to support different formatting conventions.

## Conclusion

The `NumberBase` class offers a flexible way to work with integers in various bases while preserving the base across arithmetic operations. This can be especially useful for tasks involving custom numeral systems or base conversions in Python.

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/jmtalec/NumberBase">NumberBase</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/jmtalec">Jean Moïse Talec</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
