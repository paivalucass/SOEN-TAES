import math

def count_binary_seq(n):
    count = 0
    for i in range(2**(2*n)):
        first_half = bin(i >> n).count('1')
        second_half = bin(i & (2**n-1)).count('1')
        if first_half == second_half:
            count += 1
    return count/2
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(count_binary_seq(1), 2.0, delta=0.001)

if __name__ == '__main__':
    unittest.main()