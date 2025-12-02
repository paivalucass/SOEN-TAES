from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    
    sum_of_numbers = sum(numbers)
    product_of_numbers = 1
    for num in numbers:
        product_of_numbers *= num
    
    return (sum_of_numbers, product_of_numbers)
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_non_empty_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

if __name__ == '__main__':
    unittest.main()