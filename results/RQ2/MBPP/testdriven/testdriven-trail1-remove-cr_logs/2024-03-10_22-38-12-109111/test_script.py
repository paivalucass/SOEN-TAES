def maximum(a, b):
    """
    Write a python function to find the maximum of two numbers.
    :param a: first number
    :param b: second number
    :return: maximum of the two numbers
    """
    try:
        assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Inputs should be numbers"
        return max(a, b)
    except AssertionError as e:
        return e

import unittest

class Test(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(5,10), 10)

if __name__ == '__main__':
    unittest.main()