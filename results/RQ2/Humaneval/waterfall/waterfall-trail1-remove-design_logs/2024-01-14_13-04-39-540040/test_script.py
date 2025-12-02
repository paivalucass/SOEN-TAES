from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    window = []
    
    for i, num in enumerate(numbers):
        while window and numbers[window[-1]] < num:
            window.pop()
        window.append(i)
        
        if window[0] == i - len(window):
            window.pop(0)
        
        result.append(numbers[window[0]])
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()