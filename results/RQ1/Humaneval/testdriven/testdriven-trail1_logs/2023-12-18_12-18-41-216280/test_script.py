from typing import List, Tuple
from functools import reduce

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    # Input validation
    def validate_input(numbers: List[int]) -> bool:
        return all(isinstance(num, int) for num in numbers)

    if not validate_input(numbers):
        raise ValueError("Invalid input list")

    # Calculate sum and product
    sum_result = sum(numbers)
    product_result = reduce(lambda x, y: x * y, numbers, 1)

    return (sum_result, product_result)
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))
    
    def test_non_empty_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

if __name__ == '__main__':
    unittest.main()