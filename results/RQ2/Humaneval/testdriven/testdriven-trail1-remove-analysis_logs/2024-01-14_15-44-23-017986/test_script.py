from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    window = []
    
    for i, num in enumerate(numbers):
        while window and numbers[window[-1]] <= num:
            window.pop()
        window.append(i)
        if i - window[0] >= 3:
            window.pop(0)
        result.append(numbers[window[0]])
        
    return result
import unittest
from typing import List, Tuple

class Test(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()