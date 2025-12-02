def sum_series(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    result = 0
    for i in range(n // 2 + 1):
        result += (n - 2*i)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_series(6), 12)

if __name__ == '__main__':
    unittest.main()