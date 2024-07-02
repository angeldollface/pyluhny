# PY LUHNY :iphone: :lock: :snake:

![GitHub CI](https://github.com/angeldollface/pyluhny/actions/workflows/python.yml/badge.svg)

***My implementation of the Luhn algorithm in Python. :iphone: :lock: :snake:***

## ABOUT :books:

This is my Python implementation of a package I wrote in ECMA Script and Rust a couple of weeks ago. (Link in the section below.) All of these packages do one thing: They provide functions for you to check whether the IMEI number of your smartphone is valid or not. The algorithm used here is the "Luhn" algorithm. Other implementations and web apps showcasing my implementations can be found in the section below. Enjoy. :heart:

## LINKS :earth_americas:

- Library implementation in ECMA Script: [VIEW](https://github.com/angeldollface/luhny)
- Library implementation in Rust: [VIEW](https://github.com/angeldollface/luhny.rs)

## USAGE :hammer:

### REQUIREMENTS

You should have the following tools installed and available from the command line:

- [Git](https://git-scm.org)
- [Python 3.5+](https://www.python.org/downloads/)
- Pip for Python 3.5+ (Usually comes with Python.)

### INSTALLING *PY LUHNY* ON YOUR SYSTEM

To use *Py Luhny* on your own system with your own projects, run the following command:

```bash
python -m pip install git+https://github.com/angeldollface/pyluhny
```

### IMPORTING *PY LUHNY*

To import *Py Luhny*'s functions into your Python code, add this line to the top of your code:

```python
from pyluhny import *
```

### API

- `get_index(array, item)`: Gets the index of an item in an array.
- `get_last_item(arr)`: Extracts the last item of an array and returns it.
- `remove_last(array)`: Removes the last item of an array and returns the new, changed array.
- `is_int(str)`:  Checks whether the supplied integer is an integer or not.
- `parse_int(str)`: Attempts to convert a string to an integer.
- `is_number_sequence(str)`: Checks whether the supplied digit sequence consists only of integers.
- `get_important_numbers(imei)`: Gets every second number starting from the left.
- `get_trash_numbers(imei)`: Gets all the numbers that remain. Removes the check digit because this is not allowed when adding all the remaining numbers together.
- `double_important_numbers(imei)`: Converts all the important numbers doubles them, and returns them in an array.
- `add_trash_numbers(imei)`: Adds all the remaining numbers in a lump sum.
- `convert_number_array_to_string_array(arr)`: Because this is neccessary and we cannot play fast and loose with types, we need to convert between the types of the arrays.
- `add_important_double_digits(imei)`: Splits all the characters in the important numbers and adds them all together in a lump sum.
- `validate_IMEI(imei)`: Gets the check digit of your IMEI, adds the important and the other numbers together, subtracts the mod 10 from 10 of that sum, makes a type conversion, compares the check digit and the calculated check digit, and returns true or false depending on whether they are equal or not.
- `tests()`: Tests all of the above methods.

### TEST THE EXAMPLE

To test the included example in the folder `example`, execute the following steps:

- 1.) Clone this repository to your machine:

```bash
git clone https://github.com/angeldollface/pyluhny
```

- 2.) Change directory into the repository's root:

```bash
cd pyluhny
```

- 3.) Change directory into the `example` folder:

```bash
cd example
```

- 4.) Install the example's dependencies:

```bash
python -m pip install -r requirements.txt
```

- 5.) Run the example:

```bash
python main.py
```

## CHANGELOG :black_nib:

### Version 1.0.0

- Initial release.
- Upload to GitHub.
- Getting re-acquainted with the Python eco system.

## NOTE :scroll:

- *Py Luhny :iphone: :lock: :snake:* by Alexander Abraham :black_heart: a.k.a. *"Angel Dollface" :dolls: :ribbon:*
- Licensed under the MIT license.
