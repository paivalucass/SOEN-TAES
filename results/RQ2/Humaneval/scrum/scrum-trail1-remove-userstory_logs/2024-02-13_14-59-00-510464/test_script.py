from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1
    
    sum_total = 0
    product_total = 1
    
    for num in numbers:
        if not isinstance(num, int) or num < 0:
            raise ValueError("The input list should only contain positive integers")
        
        sum_total += num
        product_total *= num
    
    return sum_total, product_total
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))
    
    def test_non_empty_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

if __name__ == '__main__':
    unittest.main()