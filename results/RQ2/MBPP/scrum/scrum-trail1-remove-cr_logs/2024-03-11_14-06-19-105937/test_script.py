def _sum(arr):
    if not arr:
        return 0
    
    total = 0
    for num in arr:
        total += num
    
    return total
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()