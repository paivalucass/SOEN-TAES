from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if not numbers or len(numbers) < 2:
        return False
    
    numbers.sort()
    
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] < threshold:
            return True
    
    return False
import unittest

class Test(unittest.TestCase):
    def test_has_close_elements(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), True)

if __name__ == '__main__':
    unittest.main()