from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input should be a list of integers")

    if not numbers:
        return (0, 1)
    
    sum_result = sum(numbers)
    product_result = 1
    for num in numbers:
        product_result *= num

    return (sum_result, product_result)
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))
        
    def test_normal_input(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

if __name__ == '__main__':
    unittest.main()