def _sum(arr):
    if not isinstance(arr, list):
        raise ValueError("Invalid input: input must be a list")
    
    if len(arr) == 0:
        return 0
    
    total = 0
    for num in arr:
        if not isinstance(num, (int, float)):
            return "Error"
        total += num
    
    return total
import unittest

class Test(unittest.TestCase):
    def test_sum_array(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()