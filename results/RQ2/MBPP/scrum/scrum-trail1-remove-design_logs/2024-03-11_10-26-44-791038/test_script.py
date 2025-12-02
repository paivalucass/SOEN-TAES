def count_binary_seq(n):
    count = 0
    for i in range(2**n):
        sum_first_n = bin(i).count('1')
        sum_last_n = bin(i << n).count('1')
        if sum_first_n == sum_last_n:
            count += 1
    return count
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()