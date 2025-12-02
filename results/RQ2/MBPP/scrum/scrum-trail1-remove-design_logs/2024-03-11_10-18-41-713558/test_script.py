import math

def harmonic_sum(n):
    result = 0.0
    for i in range(1, n+1):
        result += 1 / i
    return round(result, 15)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(harmonic_sum(7), 2.5928571428571425, delta=0.001)

if __name__ == '__main__':
    unittest.main()