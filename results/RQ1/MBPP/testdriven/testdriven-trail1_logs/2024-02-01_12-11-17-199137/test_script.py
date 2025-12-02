def sum_series(n):
    '''
    Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
    assert sum_series(6) == 12
    '''

    total_sum = 0
    for i in range(n // 2 + 1):
        total_sum += n - 2*i
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test_sum_series(self):
        self.assertEqual(sum_series(6), 12)

if __name__ == '__main__':
    unittest.main()