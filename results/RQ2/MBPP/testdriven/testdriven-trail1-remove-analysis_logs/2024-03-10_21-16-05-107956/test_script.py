def find(n, m):
    '''Write a python function to find quotient of two numbers (rounded down to the nearest integer).'''
    try:
        result = n // m
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Division by zero.")
    return result

assert find(10,3) == 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()