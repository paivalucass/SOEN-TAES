def is_polite(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"
    sum = 0
    start = 1
    for i in range(1, n + 1):
        while sum < n:
            sum += start
            start += 1
        if sum == n:
            return start
        sum -= i
    return "Error: No polite number found for the input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()