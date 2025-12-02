import math
def count_binary_seq(n):
    '''Write a function to find the count of all binary sequences of length 2n such that the sum of the first n bits is the same as the sum of the last n bits.'''
    return 2**n * math.comb(2*n, n) / (n + 1)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()