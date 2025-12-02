from collections import deque
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    window = deque()
    
    for i in range(len(numbers)):
        if window and i - window[0] == len(window):
            window.popleft()
        
        while window and numbers[window[-1]] <= numbers[i]:
            window.pop()
        
        window.append(i)
        
        result.append(numbers[window[0]])
    
    return result

import unittest
from typing import List

class Test(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()