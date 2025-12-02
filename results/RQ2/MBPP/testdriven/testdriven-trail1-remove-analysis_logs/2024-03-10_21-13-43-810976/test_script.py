import math

def harmonic_sum(n):
    if n == 0:
        return 0
    else:
        sum = 0
        for i in range(1, n+1):
            sum += 1 / i
        return round(sum, 15)

import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(harmonic_sum(7), 2.5928571428571425, delta=0.001)

if __name__ == '__main__':
    unittest.main()