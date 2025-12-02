def closest_integer(value):
    '''Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    try:
        num = float(value)
        if num > 0:
            if num - int(num) < 0.5:
                return int(num)
            else:
                return int(num) + 1
        else:
            if abs(num - int(num)) < 0.5:
                return int(num)
            else:
                return int(num) - 1
    except ValueError:
        return "Invalid input. Please enter a valid number."

# Test cases
print(closest_integer("10"))  # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("14.5"))  # Output: 15
print(closest_integer("-14.5"))  # Output: -15
print(closest_integer("0"))  # Output: 0
print(closest_integer("999999"))  # Output: 999999
print(closest_integer("-999999"))  # Output: -999999
print(closest_integer(" 10 "))  # Output: 10
print(closest_integer("!@#"))  # Output: Invalid input. Please enter a valid number.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_integer('10'), 10)
        self.assertEqual(closest_integer('15.3'), 15)
        self.assertEqual(closest_integer('14.5'), 15)
        self.assertEqual(closest_integer('-14.5'), -15)

if __name__ == '__main__':
    unittest.main()