def sum_series(n):
    result = 0
    if isinstance(n, int) and n >= 0:
        for i in range(n // 2 + 1):
            result += n - 2*i
        return result
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_series(6), 12)

if __name__ == '__main__':
    unittest.main()