def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
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
        rounded_num = round(num)
        if num - rounded_num == 0.5 or num - rounded_num == -0.5:
            return int(rounded_num + (num - rounded_num) / abs(num - rounded_num) + (0.5 if num > 0 else -0.5))
        return int(rounded_num + (num - rounded_num) / abs(num - rounded_num))
    except ZeroDivisionError:
        return "Error: Division by zero occurred."
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_integer('10'), 10)
        self.assertEqual(closest_integer('15.3'), 15)
        self.assertEqual(closest_integer('14.5'), 15)
        self.assertEqual(closest_integer('-14.5'), -15)

if __name__ == '__main__':
    unittest.main()