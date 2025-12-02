from typing import List

def is_close(num1, num2, threshold):
    if threshold < 0:
        return False
    return abs(num1 - num2) < threshold

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if len(numbers) == 0 or threshold < 0:
        return False
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if is_close(numbers[i], numbers[j], threshold):
                return True
    
    return False
import unittest

class Test(unittest.TestCase):
    def test_has_close_elements(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), True)

if __name__ == '__main__':
    unittest.main()