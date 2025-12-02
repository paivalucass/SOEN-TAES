def reverse_integer(num):
    '''
    Write a python function to reverse a given integer number.
    '''
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    if num < 0:
        raise ValueError("Input must be a positive number")

    return int(str(num)[::-1])

def is_twice_reverse_minus_one(num):
    '''
    Write a python function to check if a given number is one less than twice its reverse.
    assert is_twice_reverse_minus_one(70) == False
    '''
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    return num == 2 * reverse_integer(num) - 1

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rev(70), False)

if __name__ == '__main__':
    unittest.main()