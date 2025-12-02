import math

def harmonic_sum(n):
    if n <= 1:
        raise ValueError("n must be a positive integer greater than 1")
    result = 0.0
    for i in range(1, n+1):
        result += 1 / i
    return result
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(harmonic_sum(7), 2.5928571428571425, places=15)

if __name__ == '__main__':
    unittest.main()