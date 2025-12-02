def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        raise ValueError("x should be less than or equal to y")
    
    max_even = -1
    for num in range(x, y+1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(12, 15), 14)
        self.assertEqual(function_under_test(13, 12), -1)

if __name__ == '__main__':
    unittest.main()