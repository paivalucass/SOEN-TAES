from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    If the input list is empty, return (0, 1).
    If the input list contains negative numbers or zeros, handle the calculations accordingly.
    """
    if not numbers:
        return (0, 1)
    sum_result = 0
    prod_result = 1
    for num in numbers:
        sum_result += num
        prod_result *= num
    return (sum_result, prod_result)
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_non_empty_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

if __name__ == '__main__':
    unittest.main()