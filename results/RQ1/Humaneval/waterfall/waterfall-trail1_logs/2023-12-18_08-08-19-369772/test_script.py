from typing import List, Deque
from collections import deque

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    result = []
    window: Deque[int] = deque()

    for i, num in enumerate(numbers):
        while window and numbers[window[-1]] < num:
            window.pop()

        window.append(i)

        if i - window[0] + 1 > len(numbers):
            window.popleft()

        result.append(numbers[window[0]])

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()