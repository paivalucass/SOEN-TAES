from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    def is_close(num1: float, num2: float, threshold: float) -> bool:
        return abs(num1 - num2) <= threshold
    
    def has_close_pair(numbers: List[float], threshold: float) -> bool:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if is_close(numbers[i], numbers[j], threshold):
                    return True
        return False
    
    return has_close_pair(numbers, threshold)
import unittest

from typing import List


class Test(unittest.TestCase):
    def test_has_close_elements(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), True)


if __name__ == '__main__':
    unittest.main()