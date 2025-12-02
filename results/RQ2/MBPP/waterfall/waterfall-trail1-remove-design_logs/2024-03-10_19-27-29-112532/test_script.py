def _sum(arr):
    if not arr:
        return 0
    if not all(isinstance(x, (int, float)) for x in arr):
        return "Invalid input: array must contain only numbers"
    
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()