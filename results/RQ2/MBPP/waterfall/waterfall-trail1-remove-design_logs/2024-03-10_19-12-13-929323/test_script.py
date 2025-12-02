def count_no_of_ways(n, k):
    if n < 0 or k <= 0 or not isinstance(k, int):
        raise ValueError("n must be a non-negative integer and k must be a positive integer")
    
    if n == 0:
        return 0
    
    same, diff = 0, k
    
    for _ in range(1, n):
        same, diff = diff, (same + diff) * (k - 1)
    
    return same + diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_no_of_ways(2, 4), 16)

if __name__ == '__main__':
    unittest.main()