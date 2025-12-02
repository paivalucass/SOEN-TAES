from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input list must contain only integers")

    if not numbers:
        return 0, 1

    product = 1
    for num in numbers:
        product *= num

    return sum(numbers), product
import unittest
from typing import List, Tuple

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))
    
    def test_non_empty_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

if __name__ == '__main__':
    unittest.main()