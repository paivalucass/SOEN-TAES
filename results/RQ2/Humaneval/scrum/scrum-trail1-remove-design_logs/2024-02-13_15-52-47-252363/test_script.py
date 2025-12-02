from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    maximum = float('-inf')
    for num in numbers:
        maximum = max(maximum, num)
        result.append(maximum)
    return result
import unittest
from typing import List, Tuple

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()