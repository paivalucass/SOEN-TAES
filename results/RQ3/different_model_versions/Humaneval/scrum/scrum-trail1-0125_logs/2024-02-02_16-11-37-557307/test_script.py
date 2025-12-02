from typing import List, Deque
from collections import deque

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    result = []
    queue = deque()
    for i in range(len(numbers)):
        if queue and queue[0] == i - len(numbers):
            queue.popleft()
        while queue and numbers[queue[-1]] < numbers[i]:
            queue.pop()
        queue.append(i)
        result.append(numbers[queue[0]])
    return result
import unittest

from typing import List, Tuple

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()