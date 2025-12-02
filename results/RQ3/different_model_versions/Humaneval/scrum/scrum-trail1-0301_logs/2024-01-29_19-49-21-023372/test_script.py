from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")
        
    numbers.sort()
    min_distance = float('inf')
    closest_pair = None
    
    for i in range(len(numbers)-1):
        dist = numbers[i+1] - numbers[i]
        if dist < min_distance:
            min_distance = dist
            closest_pair = (numbers[i], numbers[i+1])
            
    if closest_pair is None:
        raise ValueError("Could not find closest pair.")
        
    return closest_pair
import unittest

from typing import List, Tuple

class Test(unittest.TestCase):
    def test_find_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
        self.assertEqual(find_closest_elements([1.0, 1.2, 2.0, 3.0, 4.0, 5.0]), (1.0, 1.2))
        self.assertEqual(find_closest_elements([5.0, 4.0, 3.0, 2.0, 1.0]), (1.0, 2.0))
        with self.assertRaises(ValueError):
            find_closest_elements([1.0])

if __name__ == '__main__':
    unittest.main()