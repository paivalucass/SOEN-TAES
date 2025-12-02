from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(max(numbers[:i+1]))
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()