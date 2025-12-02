from typing import List, Tuple
from functools import reduce

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if len(numbers) == 0:
        return (0, 1)
    else:
        s = sum(numbers)
        p = reduce(lambda x, y: x * y, numbers)
        return (s, p)

import unittest

from typing import List, Tuple

class Test(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_number(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

if __name__ == '__main__':
    unittest.main()