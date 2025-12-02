def harmonic_sum(n):
    sum = 0.0
    for i in range(1, n+1):
        sum += 1 / i
    return sum
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(harmonic_sum(7), 2.5928571428571425, delta=0.001)

if __name__ == '__main__':
    unittest.main()