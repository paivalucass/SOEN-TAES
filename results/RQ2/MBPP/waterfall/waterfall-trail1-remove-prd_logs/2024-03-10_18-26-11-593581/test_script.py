def smallest_num(xs):
    '''Function to find the smallest number in a list.'''
    if len(xs) == 0:
        return None  # Handle empty input
    try:
        return min(xs)  # Find the smallest number
    except (TypeError, ValueError):
        return None  # Handle non-numeric input

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()