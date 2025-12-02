from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two numbers")
    
    numbers.sort()
    min_difference = float('inf')
    result_pair = ()
    
    for i in range(len(numbers) - 1):
        difference = abs(numbers[i] - numbers[i+1])
        if difference < min_difference:
            min_difference = difference
            result_pair = (numbers[i], numbers[i+1])
    
    return result_pair
import unittest
from typing import List, Tuple

class Test(unittest.TestCase):
    def test_find_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

if __name__ == '__main__':
    unittest.main()