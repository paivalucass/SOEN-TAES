from typing import List, Tuple
from collections import deque

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    if len(numbers) == 1:
        return numbers
    
    result = []
    q = deque()
    
    for i, num in enumerate(numbers):
        while q and numbers[q[-1]] < num:
            q.pop()
        q.append(i)
        
        if q[0] == i - len(numbers):
            q.popleft()
            
        result.append(numbers[q[0]])
    
    return result

import unittest

class Test(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()