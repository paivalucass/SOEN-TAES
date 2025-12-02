from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    window = []
    for i in range(len(numbers)):
        if i < 3:
            result.append(numbers[i])
        else:
            result.append(max(numbers[i-3:i+1]))
    return result
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()