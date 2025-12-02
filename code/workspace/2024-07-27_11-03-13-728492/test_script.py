from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    visited = set()
    for i in range(len(numbers)):
        if numbers[i] in visited:
            continue
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
        visited.add(numbers[i])
    return False
import unittest

class Test(unittest.TestCase):
    def test_has_close_elements(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), True)

if __name__ == '__main__':
    unittest.main()