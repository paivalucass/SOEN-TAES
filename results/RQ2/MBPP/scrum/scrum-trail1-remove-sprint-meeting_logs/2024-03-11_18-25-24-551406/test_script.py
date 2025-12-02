def sum_series(n):
    '''This function calculates the sum of (n - 2*i) from i=0 to n // 2.'''
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    result = 0
    for i in range(n // 2 + 1):
        result += n - 2*i

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_series(6), 12)

if __name__ == '__main__':
    unittest.main()