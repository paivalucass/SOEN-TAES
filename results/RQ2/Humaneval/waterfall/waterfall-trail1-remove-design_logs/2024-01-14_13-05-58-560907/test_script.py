from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if not numbers:
        return ()
    
    numbers = sorted(numbers)
    min_diff = float('inf')
    result = ()
    
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i], numbers[i+1])
    
    return result
import unittest
from typing import List, Tuple


class Test(unittest.TestCase):
    def test_find_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

if __name__ == '__main__':
    unittest.main()