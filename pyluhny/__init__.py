# PY LUHNY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

def get_index(array, item):
    """
    Gets the index of an item in an array.
    """
    return array.index(item)

def get_last_item(arr):
   """
   Extracts the last item of
   an array and returns it.
   """
   return arr[-1]

def remove_last(array):
    """
    Removes the last item of an array
    and returns the new, changed array.
    """
    array.pop(-1)
    return array

def is_int(str):
    """
    Checks whether the supplied
    integer is an integer or not.
    """
    result = True
    try:
        int(str)
    except Exception as error:
        result = False
    return result

def parse_int(str):
    """
    Attempts to convert a string to
    an integer.
    """
    result = 0
    if is_int(str):
        result = int(str)
    else:
        pass
    return result

def is_number_sequence(str):
    """
    Checks whether the supplied digit
    sequence consists only of integers.
    """
    result = True
    for i in list(str):
        if is_int(str):
            pass
        else:
            result = False
    return result

def get_important_numbers(imei):
    """
    Gets every second number 
    starting from the left.
    """
    result = []
    for index, entry in enumerate(list(imei)):
        if index%2 != 0:
            result.append(entry)
        else:
            pass
    return result

def get_trash_numbers(imei):
    """
    Gets all the numbers that remain. 
    Removes the check digit because this is not 
    allowed when adding all the remaining 
    numbers together.
    """
    result = []
    for index, entry in enumerate(list(imei)):
        if index%2 != 0:
            pass
        else:
            result.append(entry)
    result.pop(-1)
    return result

def double_important_numbers(imei):
    """
    Converts all the important numbers, 
    doubles them, and returns them
    in an array.
    """
    important_nums = get_important_numbers(imei)
    result = []
    for i in important_nums:
        result.append(parse_int(i)*2)
    return result

def add_trash_numbers(imei):
    """
    Adds all the remaining 
    numbers in a lump sum.
    """
    trash_nums = get_trash_numbers(imei)
    result = 0
    for i in trash_nums:
        result = result + parse_int(i);
    return result

def convert_number_array_to_string_array(arr):
    result = []
    for item in arr:
        num = str(item)
        nums = list(num)
        for x in nums:
            result.append(x)
    return result


def add_important_double_digits(imei):
    """
    Splits all the characters in the 
    important numbers and adds them all
    together in a lump sum.
    """
    result = 0
    doubles = double_important_numbers(imei)
    digit_arr = convert_number_array_to_string_array(doubles)
    for item in digit_arr:
        result = result + parse_int(item)
    return result

def validate_IMEI(imei):
    """
    Gets the check digit of your IMEI, 
    adds the important and the
    other numbers together, subtracts 
    the mod 10 from 10 of that sum, makes
    a type conversion, compares the check 
    digit and the calculated check digit,
    and returns true or false depending 
    on whether they are equal or not.
    """
    result = True
    std_length = 15;
    imei_chars = list(imei)
    check_digit = get_last_item(imei_chars)
    sum = add_important_double_digits(imei) + add_trash_numbers(imei)
    computed_check_digit = 10 - (sum%10)
    computed_converted_check_digit = str(computed_check_digit)
    if check_digit == computed_converted_check_digit and len(imei_chars) == std_length and is_number_sequence(imei):
        pass
    else:
        result = False
    return result

def tests():
    """
    Tests all of the above methods.
    """
    test_int = '2'
    test_letter= 'A'
    number_arr = ['1','2','3']
    test_imei = '353879234252633'
    fake_imei = '356728113476859'
    too_long_imei = '3567281134768579'
    non_numeric_imei = '356728113476A59'
    print(remove_last(number_arr))
    print(is_int(test_int))
    print(is_int(test_letter))
    print(parse_int(test_int))
    print(parse_int(test_letter))
    print(validate_IMEI(test_imei))
    print(validate_IMEI(fake_imei))
    print(validate_IMEI(too_long_imei))
    print(validate_IMEI(non_numeric_imei))